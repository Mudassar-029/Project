import cv2
import numpy as np
from pywt import dwt2
import pywt

cap=cv2.VideoCapture(0)
ret,frame = cap.read()
cv2.imshow('frame',frame)

img_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) 


_, (cH, cV, cD) = dwt2(img_hsv.T, 'db1')
# a - LL, h - LH, v - HL, d - HH as in matlab
Energy = (cH**2 + cV**2 + cD**2).sum()/img_hsv.size

print("Energy",Energy)

while True:
 k = cv2.waitKey(0) & 0xFF     
 if k == 27: break  
 cv2.destroyAllWindows()
cap.release()