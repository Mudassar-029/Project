import cv2
import numpy as np

cap=cv2.VideoCapture(0)
ret,frame = cap.read()

img_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) 

cv2.imshow('frame',frame)
cv2.imshow("Hsv",img_hsv)

while True:
 k = cv2.waitKey(0) & 0xFF     
 if k == 27: break  
 cv2.destroyAllWindows()
cap.release()
