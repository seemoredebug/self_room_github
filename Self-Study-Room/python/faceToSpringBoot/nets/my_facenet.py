
import torch.nn as nn
from torch.nn import functional as F
from torch.hub import load_state_dict_from_url
from nets.my_mobilenet import  MobileNetV1



class mobilenet(nn.Module):
    def __init__(self, pretrained):
        super(mobilenet, self).__init__()
        self.model = MobileNetV1()
        if pretrained:
            state_dict = load_state_dict_from_url(r"backbone_weights_of_mobilenetv1.pth", model_dir="model_data",
                                                progress=True)
            self.model.load_state_dict(state_dict)

        del self.model.fc
        del self.model.avg

    def forward(self, x):
        x = self.model.stage1(x)
        x = self.model.stage2(x)
        x = self.model.stage3(x)
        return x   
        
class Facenet(nn.Module):
    def __init__(self, backbone="mobilenet", dropout_keep_prob=0.5, embedding_size=128, num_classes=None, mode="train", pretrained=False):
        super(Facenet, self).__init__()
        # if backbone == "mobilenet": # 选择模型
        self.backbone = mobilenet(pretrained)#导入模型
        flat_shape = 1024
        # elif backbone == "inception_resnetv1":
        #     self.backbone = inception_resnet(pretrained)
        #     flat_shape = 1792
        # else:
        #     raise ValueError('Unsupported backbone - `{}`, Use mobilenet, inception_resnetv1.'.format(backbone))
        #全局的平均池化 降低参数量，全局平均池化层没有参数，可防止在该层过拟合
        self.avg        = nn.AdaptiveAvgPool2d((1,1))
        # dropout随机丢弃防止过拟合
        self.Dropout    = nn.Dropout(1 - dropout_keep_prob)
        # 全连接层 为1*1*128
        self.Bottleneck = nn.Linear(flat_shape, embedding_size,bias=False)
        # 标准化为128
        self.last_bn    = nn.BatchNorm1d(embedding_size, eps=0.001, momentum=0.1, affine=True)
        if mode == "train":
            # 加入Cross-Entropy Loss用于人脸分类辅助收敛。对num_classes种进行分类
            self.classifier = nn.Linear(embedding_size, num_classes)

    def forward(self, x):
        x = self.backbone(x) # 导入mobilenet模型 得到5*5*1204的特征矩阵
        x = self.avg(x)# 全局的平均池化 得到1*1*1024
        x = x.view(x.size(0), -1) # batch.size 第一维度为1204的特征向量
        x = self.Dropout(x) # dropout随机丢弃防止过拟合
        x = self.Bottleneck(x) # 全连接层为1*1*128
        x = self.last_bn(x)# 标准化 得到128

        #L2标准化 p==2表示进行L2标准化 dim表示第几维度
        x = F.normalize(x, p=2, dim=1)
        return x

    def forward_feature(self, x):
        x = self.backbone(x)
        x = self.avg(x)
        x = x.view(x.size(0), -1)
        x = self.Dropout(x)
        x = self.Bottleneck(x)
        before_normalize = self.last_bn(x)
        x = F.normalize(before_normalize, p=2, dim=1)
        return before_normalize, x

    def forward_classifier(self, x):
        x = self.classifier(x)
        return x