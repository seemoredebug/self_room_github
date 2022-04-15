import cv2

img3ChaCom = cv2.imread('test/190308010333.png', cv2.IMREAD_UNCHANGED)
cv2.imshow('IMREAD_UNCHANGED+Color',img3ChaCom)
cv2.waitKey()