import cv2
img = cv2.imread('redd.png')
cv2.line(img,(0,0),(512,512),color=(0,0,255),thickness=3)
cv2.line(img,(0,512),(512,0),color=(255,0,255),thickness=3)
cv2.imshow("img",img)
cv2.waitKey(0)