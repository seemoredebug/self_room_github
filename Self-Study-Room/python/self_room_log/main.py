from PIL import Image

from interFaceData import Facenet
faceNet = Facenet()
# faceNet.interFaceData(r"test\1.png", "190308010333")
data = faceNet.outFaceData()

image_1 = Image.open()