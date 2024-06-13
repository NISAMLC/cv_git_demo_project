import cv2
img = cv2.imread('redd.png')
cv2.line(img,(0,0),(512,512),color=(0,0,255),thickness=3)
##new_intro
cv2.line(img,(256,0),(256,512),color=(255,255,255),thickness=4)
cv2.circle(img,(100,300),80,color=(255,255,255),thickness=4)
##
cv2.imshow("img",img)
cv2.waitKey(0)