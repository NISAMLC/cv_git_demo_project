import cv2
img = cv2.imread('redd.png')
cv2.line(img,(0,0),(512,512),color=(0,0,255),thickness=3)
cv2.putText(img,("Its lana's Image Right?"),(100,200),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,25
                                                                                                           0,200),thickness=3)
cv2.imshow("img",img)
cv2.waitKey(0)