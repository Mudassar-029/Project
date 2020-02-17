import cv2
import numpy as np

cap=cv2.VideoCapture(0)
ret,frame = cap.read()

img_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) 

hsv_lower = np.array([41,57,78])
hsv_upper = np.array([145,255,255])

mask = cv2.inRange(img_hsv, hsv_lower, hsv_upper)
mask_inv = cv2.bitwise_not(mask)
result = cv2.bitwise_and(frame, frame, mask= mask_inv)

cv2.imshow('frame',frame)
# cv2.imshow("Hsv",img_hsv)
cv2.imshow("result",result)


while True:
 k = cv2.waitKey(0) & 0xFF     
 if k == 27: break  
 cv2.destroyAllWindows()
cap.release()