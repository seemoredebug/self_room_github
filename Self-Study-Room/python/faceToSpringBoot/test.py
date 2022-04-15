import os

import numpy as np

from retinaface import Retinaface
from face_mysql.Face_Mysql import Face_Mysql
'''
在更换facenet网络后一定要重新进行人脸编码，运行encoding.py。
'''

retinaface = Retinaface(1)
fm = Face_Mysql()

list_dir = os.listdir("face_dataset")
image_paths = []
names = []
for name in list_dir:
    image_paths.append("face_dataset/"+name)
    names.append(name.split("_")[0])

label,datas=retinaface.testencode_face_dataset(image_paths,names)
for i in range(datas.__len__()):
    fm.in_mysql(label[i],datas[i].tolist())

outlabel,outdatas=fm.out_mysql()

for i in range(outdatas.__len__()):
    print(outlabel[i],"    ",outdatas[i])