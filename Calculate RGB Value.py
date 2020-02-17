import cv2
import numpy as np

cap=cv2.VideoCapture(0)
ret,frame = cap.read()
cv2.imshow('frame',frame)

img_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) 

hsv_lower = np.array([41,57,78])
hsv_upper = np.array([145,255,255])

mask = cv2.inRange(img_hsv, hsv_lower, hsv_upper)
mask_inv = cv2.bitwise_not(mask)
result = cv2.bitwise_and(frame, frame, mask= mask_inv)

kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(mask_inv, cv2.MORPH_OPEN, kernel)
op = cv2.bitwise_and(frame, frame, mask= opening)

closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
closing = cv2.bitwise_and(frame, frame, mask= closing)


blur = cv2.GaussianBlur(closing,(15,15),1)


RGB_color = blur[255, 255]
print("RGB =",RGB_color )
B = blur[255,255,0]
G = blur[255,255,1]
R= blur[255,255,2]
 
blue_per=np.round(B/(B+G+R)*100 ,2) 
print("Blue pixel percentage =",blue_per,"%")

green_per=np.round(G/(B+G+R)*100 ,2) 
print("Green pixel percentage = ",green_per ,"%")

red_per=np.round(R/(B+G+R)*100 ,2) 
print("Red pixel percentage =", red_per,"%")


while True:
 k = cv2.waitKey(0) & 0xFF     
 if k == 27: break  
 cv2.destroyAllWindows()
cap.release()