import cv2
import numpy as np
import torch
from PIL import Image

from interFaceData import Facenet


def inData(fileurl,score):
    facenet = Facenet()
    facenet.interFaceData(fileurl,score)
    return "OK!!!"

def getFace(fileurl,score):
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    framebf = cv2.imread(fileurl,cv2.IMREAD_UNCHANGED)
    frame =np.asarray(framebf)
    # framebf = torch.from_numpy(np.expand_dims(np.transpose(np.array(framebf, np.float32) / 255, (2, 0, 1)), 0))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 调用分类器进行检测
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=7,
        minSize=(96, 116),
        # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    # 画矩形框
    for (x, y, w, h) in faces:
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        flog2 = 0
        img2 = framebf[int(y):(int(y) + int(h)), int(x):(int(x) + int(w))]
        img2 = framebf[y:y + h, x:x + h, :]
        # img2 = img2[0:112,0:96,:3]
        imgurl = "./test/"+score+"-face.png"
        cv2.imwrite(imgurl, img2)
    if(imgurl):
        return imgurl
    else:
        return "false";

if __name__ == '__main__':
    fileurl=input()
    score=input()
    fileurl=getFace(fileurl,score)
    if(fileurl!="false"):
        inData(fileurl,score)