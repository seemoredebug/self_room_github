from PIL import Image

from interFaceData import Facenet

if __name__ == '__main__':
    import cv2
    import sys
    import logging as log
    import datetime as dt
    from time import sleep

    model = Facenet()

    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    # 打开视频捕获设备
    video_capture = cv2.VideoCapture(0)

    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass

    # 读视频帧
        ret, frame = video_capture.read()
    # 转为灰度图像
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
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            flog2 = 0
            img2 = frame[int(y):(int(y) + int(h)), int(x):(int(x) + int(w))]
            img2 = frame[y:y+h, x:x+h,:]
            # img2 = img2[0:112,0:96,:3]
            cv2.imshow('image', img2)
            cv2.imwrite("./test/2.png", img2)
            img2 = Image.open("./test/2.png")
            data,label =model.outFaceData()
            newdata = model.matrix_128(img2)
            probability=model.getImageLL(data[0],newdata)
            labelnow=label[0]
            for i in range(data.__len__()):
                now = model.getImageLL(data[i],newdata) # 差距越大越不是本人 阈值设置为0.9
                if(now<probability):
                    probability=now
                    labelnow=label[i]
            # if(probability<0.9):
            print(str(labelnow)+"      "+str(probability))
            cv2.putText(frame, str(labelnow), (x, y - 10), cv2.FONT_HERSHEY_TRIPLEX, (x-w) / 120, (0, 255, 0), 2)
            # print(probability)
        # if flog==0:
        #     flog=1
        #     print(frame)
        #     cv2.imshow('image', frame)

        # if flog2 == 0:
        #     imwrite("./test/1.png", frame)
        #     flog2 = 1
    # 显示视频
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 关闭摄像头设备
    video_capture.release()

    # 关闭所有窗口
    cv2.destroyAllWindows()