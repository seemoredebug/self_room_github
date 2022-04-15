import os

import numpy as np
import sys
# import torch.jit
from retinaface import Retinaface
from face_mysql.Face_Mysql import Face_Mysql
#
# def script_method(fn, _rcb=None):
#     return fn
# def script(obj, optimize=True, _frames_up=0, _rcb=None):
#     return obj



if __name__ == '__main__':
    # torch.jit.script_method = script_method
    # torch.jit.script = script

    os.environ["PYTORCH_JIT"] = "0"
    retinaface = Retinaface(1)
    fm = Face_Mysql()

    image_paths = []
    names = []
    image_paths.append(sys.argv[1])
    names.append(sys.argv[2])

    print(image_paths)
    print(names)
    label,datas=retinaface.testencode_face_dataset(image_paths,names)
    for i in range(datas.__len__()):
        fm.in_mysql(label[i],datas[i].tolist())
        fm.inFaceURL(label[i],image_paths[i])
