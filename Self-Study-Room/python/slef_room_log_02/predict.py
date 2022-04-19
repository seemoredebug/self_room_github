#----------------------------------------------------#
#   对视频中的predict.py进行了修改，
#   将单张图片预测、摄像头检测和FPS测试功能
#   整合到了一个py文件中，通过指定mode进行模式的修改。
#----------------------------------------------------#
from datetime import datetime
import time

import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw

from retinaface import Retinaface

if __name__ == "__main__":
    retinaface = Retinaface()

    capture = cv2.VideoCapture(0)

    ref, frame = capture.read()
    if not ref:
        raise ValueError("未能正确读取摄像头（视频），请注意是否正确安装摄像头（是否正确填写视频路径）。")

    fps = 0.0
    last_detected = datetime.now()
    true_name="初始化"
    while(True):
            t1 = time.time()
            # 读取某一帧
            ref, frame = capture.read()
            if not ref:
                break
            # 格式转变，BGRtoRGB
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            # 进行检测
            # frame = np.array(retinaface.detect_image(frame))
            #
            name,isrignt=retinaface.detect_image(frame)

            if (name != "Unknown"):
                if (isrignt):
                    name += "TRUE"
                else:
                    name += "False"
                last_detected = datetime.now()
                true_name=name


            if (datetime.now() - last_detected).total_seconds() < 2:
                frame = cv2.putText(frame, true_name, (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                # label = true_name.encode('utf-8')
                # img = Image.fromarray(np.uint8(frame))
                # # ---------------#
                # #   设置字体
                # # ---------------#
                # font = ImageFont.truetype(font='model_data/simhei.ttf', size=30)
                # draw = ImageDraw.Draw(img)
                # textColor = (255, 255, 255)
                # draw.text((100, 100), str(true_name, 'UTF-8'), fill=textColor, font=font)
                # frame = np.array(np.asarray(img))

            # frame = np.array()
            # RGBtoBGR满足opencv显示格式
            frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
                    
            fps  = ( fps + (1./(time.time()-t1)) ) / 2
            print("fps= %.2f"%(fps))
            frame = cv2.putText(frame, "fps= %.2f"%(fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            cv2.imshow("video",frame)
            c= cv2.waitKey(1) & 0xff

            if c==27:
                capture.release()
                break
    print("Video Detection Done!")
    capture.release()
    cv2.destroyAllWindows()

