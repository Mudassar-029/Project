import cv2
import numpy as np
cap=cv2.VideoCapture(0)
ret,frame = cap.read()
cv2.imshow('frame',frame)
while True:
 k = cv2.waitKey(0) & 0xFF     
 if k == 27: break  
 cv2.destroyAllWindows()
cap.release()