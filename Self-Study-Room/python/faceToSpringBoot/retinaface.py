import numpy as np
import torch
import torch.nn as nn
from PIL import Image
from tqdm import tqdm

from nets.my_facenet  import Facenet
from nets_retinaface.retinaface import RetinaFace
from utils.anchors import Anchors
from utils.config import cfg_mnet
from utils.utils import (Alignment_1, letterbox_image,
                         preprocess_input)
from utils.utils_bbox import (decode, decode_landm, non_max_suppression,
                              retinaface_correct_boxes)
from face_mysql.Face_Mysql import Face_Mysql

#--------------------------------------#
#   一定注意backbone和model_path的对应。
#   在更换facenet_model后，
#   一定要注意重新编码人脸。
#--------------------------------------#
class Retinaface(object):
    _defaults = {
        #----------------------------------------------------------------------#
        #   retinaface训练完的权值路径
        #----------------------------------------------------------------------#
        "retinaface_model_path" : 'model_data/Retinaface_mobilenet0.25.pth',
        #----------------------------------------------------------------------#
        #   retinaface所使用的主干网络，有mobilenet和resnet50
        #----------------------------------------------------------------------#
        "retinaface_backbone"   : "mobilenet",
        #----------------------------------------------------------------------#
        #   retinaface中只有得分大于置信度的预测框会被保留下来
        #----------------------------------------------------------------------#
        "confidence"            : 0.5,
        #----------------------------------------------------------------------#
        #   retinaface中非极大抑制所用到的nms_iou大小
        #----------------------------------------------------------------------#
        "nms_iou"               : 0.3,
        #----------------------------------------------------------------------#
        #   是否需要进行图像大小限制。
        #   输入图像大小会大幅度地影响FPS，想加快检测速度可以减少input_shape。
        #   开启后，会将输入图像的大小限制为input_shape。否则使用原图进行预测。
        #   会导致检测结果偏差，主干为resnet50不存在此问题。
        #   可根据输入图像的大小自行调整input_shape，注意为32的倍数，如[640, 640, 3]
        #----------------------------------------------------------------------#
        "retinaface_input_shape": [640, 640, 3],
        #----------------------------------------------------------------------#
        #   是否需要进行图像大小限制。
        #----------------------------------------------------------------------#
        "letterbox_image"       : True,
        
        #----------------------------------------------------------------------#
        #   facenet训练完的权值路径
        #----------------------------------------------------------------------#
        "facenet_model_path"    : 'model_data/facenet_mobilenet.pth',
        #----------------------------------------------------------------------#
        #   facenet所使用的主干网络， mobilenet和inception_resnetv1
        #----------------------------------------------------------------------#
        "facenet_backbone"      : "mobilenet",
        #----------------------------------------------------------------------#
        #   facenet所使用到的输入图片大小
        #----------------------------------------------------------------------#
        "facenet_input_shape"   : [160, 160, 3],
        #----------------------------------------------------------------------#
        #   facenet所使用的人脸距离门限
        #----------------------------------------------------------------------#
        "facenet_threhold"      : 0.9,

        #--------------------------------#
        #   是否使用Cuda
        #   没有GPU可以设置成False
        #--------------------------------#
        "cuda"                  : False
    }

    @classmethod
    def get_defaults(cls, n):
        if n in cls._defaults:
            return cls._defaults[n]
        else:
            return "Unrecognized attribute name '" + n + "'"

    #---------------------------------------------------#
    #   初始化Retinaface
    #---------------------------------------------------#
    def __init__(self, encoding=0, **kwargs):
        self.__dict__.update(self._defaults)
        for name, value in kwargs.items():
            setattr(self, name, value)

        #---------------------------------------------------#
        #   不同主干网络的config信息
        #---------------------------------------------------#
        if self.retinaface_backbone == "mobilenet":
            self.cfg = cfg_mnet

        #---------------------------------------------------#
        #   先验框的生成
        #---------------------------------------------------#
        self.anchors = Anchors(self.cfg, image_size=(self.retinaface_input_shape[0], self.retinaface_input_shape[1])).get_anchors()
        self.generate()

        fm=Face_Mysql()
        try:
            self.known_face_names,self.known_face_encodings=fm.out_mysql()
        except:
            if not encoding:
                print("载入已有人脸特征失败，请检查model_data下面是否生成了相关的人脸特征文件。")
            pass
    #---------------------------------------------------#
    #   获得所有的分类
    #---------------------------------------------------#
    def generate(self):
        #-------------------------------#
        #   载入模型与权值
        #-------------------------------#
        self.net        = RetinaFace(cfg=self.cfg, phase='eval', pre_train=False).eval()
        self.facenet    = Facenet(backbone=self.facenet_backbone, mode="predict").eval()

        print('Loading weights into state dict...')
        state_dict = torch.load(self.retinaface_model_path)
        self.net.load_state_dict(state_dict)

        state_dict = torch.load(self.facenet_model_path)
        self.facenet.load_state_dict(state_dict, strict=False)

        # if self.cuda:
        #     self.net = nn.DataParallel(self.net)
        #     self.net = self.net.cuda()
        #
        #     self.facenet = nn.DataParallel(self.facenet)
        #     self.facenet = self.facenet.cuda()
        print('Finished!')


    def testencode_face_dataset(self, image_paths, names):
        face_encodings = []
        for index, path in enumerate(tqdm(image_paths)):
            #---------------------------------------------------#
            #   打开人脸图片
            #---------------------------------------------------#
            image       = np.array(Image.open(path), np.float32)
            #---------------------------------------------------#
            #   对输入图像进行一个备份
            #---------------------------------------------------#
            old_image   = image.copy()
            #---------------------------------------------------#
            #   计算输入图片的高和宽
            #---------------------------------------------------#
            im_height, im_width, _ = np.shape(image)
            #---------------------------------------------------#
            #   计算scale，用于将获得的预测框转换成原图的高宽
            #---------------------------------------------------#
            scale = [
                np.shape(image)[1], np.shape(image)[0], np.shape(image)[1], np.shape(image)[0]
            ]
            scale_for_landmarks = [
                np.shape(image)[1], np.shape(image)[0], np.shape(image)[1], np.shape(image)[0],
                np.shape(image)[1], np.shape(image)[0], np.shape(image)[1], np.shape(image)[0],
                np.shape(image)[1], np.shape(image)[0]
            ]
            if self.letterbox_image:
                image = letterbox_image(image, [self.retinaface_input_shape[1], self.retinaface_input_shape[0]])
                anchors = self.anchors
            else:
                anchors = Anchors(self.cfg, image_size=(im_height, im_width)).get_anchors()

            #---------------------------------------------------#
            #   将处理完的图片传入Retinaface网络当中进行预测
            #---------------------------------------------------#
            with torch.no_grad():
                #-----------------------------------------------------------#
                #   图片预处理，归一化。
                #-----------------------------------------------------------#
                image = torch.from_numpy(preprocess_input(image).transpose(2, 0, 1)).unsqueeze(0).type(torch.FloatTensor)

                # if self.cuda:
                #     image               = image.cuda()
                #     anchors             = anchors.cuda()

                loc, conf, landms = self.net(image)
                #-----------------------------------------------------------#
                #   对预测框进行解码
                #-----------------------------------------------------------#
                boxes   = decode(loc.data.squeeze(0), anchors, self.cfg['variance'])
                #-----------------------------------------------------------#
                #   获得预测结果的置信度
                #-----------------------------------------------------------#
                conf    = conf.data.squeeze(0)[:, 1:2]
                #-----------------------------------------------------------#
                #   对人脸关键点进行解码
                #-----------------------------------------------------------#
                landms  = decode_landm(landms.data.squeeze(0), anchors, self.cfg['variance'])

                #-----------------------------------------------------------#
                #   对人脸检测结果进行堆叠
                #-----------------------------------------------------------#
                boxes_conf_landms = torch.cat([boxes, conf, landms], -1)
                boxes_conf_landms = non_max_suppression(boxes_conf_landms, self.confidence)

                if len(boxes_conf_landms) <= 0:
                    print(names[index], "：未检测到人脸")
                    continue
                #---------------------------------------------------------#
                #   如果使用了letterbox_image的话，要把灰条的部分去除掉。
                #---------------------------------------------------------#
                if self.letterbox_image:
                    boxes_conf_landms = retinaface_correct_boxes(boxes_conf_landms, \
                        np.array([self.retinaface_input_shape[0], self.retinaface_input_shape[1]]), np.array([im_height, im_width]))

            boxes_conf_landms[:, :4] = boxes_conf_landms[:, :4] * scale
            boxes_conf_landms[:, 5:] = boxes_conf_landms[:, 5:] * scale_for_landmarks

            #---------------------------------------------------#
            #   选取最大的人脸框。
            #---------------------------------------------------#
            best_face_location  = None
            biggest_area        = 0
            for result in boxes_conf_landms:
                left, top, right, bottom = result[0:4]

                w = right - left
                h = bottom - top
                if w * h > biggest_area:
                    biggest_area = w * h
                    best_face_location = result

            #---------------------------------------------------#
            #   截取图像
            #---------------------------------------------------#
            crop_img = old_image[int(best_face_location[1]):int(best_face_location[3]), int(best_face_location[0]):int(best_face_location[2])]
            landmark = np.reshape(best_face_location[5:],(5,2)) - np.array([int(best_face_location[0]),int(best_face_location[1])])
            crop_img,_ = Alignment_1(crop_img,landmark)

            crop_img = np.array(letterbox_image(np.uint8(crop_img),(self.facenet_input_shape[1],self.facenet_input_shape[0])))/255
            crop_img = crop_img.transpose(2, 0, 1)
            crop_img = np.expand_dims(crop_img,0)
            #---------------------------------------------------#
            #   利用图像算取长度为128的特征向量
            #---------------------------------------------------#
            with torch.no_grad():
                crop_img = torch.from_numpy(crop_img).type(torch.FloatTensor)
                # if self.cuda: linux没有显卡 删除
                #     crop_img = crop_img.cuda()

                face_encoding = self.facenet(crop_img)[0].cpu().numpy()
                face_encodings.append(face_encoding)
        return names,face_encodings
