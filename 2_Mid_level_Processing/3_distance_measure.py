import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 
import math
 
img=cv.imread('C:/Users/imrk0/Desktop/CV/0_img/building.jpg',1)
 
ret,thresh=cv.threshold(img.copy(),38,255,cv.THRESH_BINARY)
canny = cv.Canny(thresh, 100, 200)
 
corners = cv.goodFeaturesToTrack(canny,10,0.4,5)
corners=np.int0(corners)
flag1=False
x1=0
y1=0
x2=0
y2=0
for corner in corners:
    x,y = corner.ravel()
    if img[x,y][0]!=0 and (img[x,y][1]!=0 and img[x,y][2]!=0):
        
        if (flag1!=True):
            x1=x.item()
            y1=y.item() 
            cv.circle(img,(x,y),5,(0,255,255),-1)
            flag1=True
        elif (img[x,y][0] != img[x1,y1][0]) and ((img[x,y][1] != img[x1,y1][1]) and (img[x,y][2] != img[x1,y1][2])) :
            x2=x.item()
            y2=y.item() 
            cv.circle(img,(x,y),5,(0,255,255),-1)
            break
        
# cv.imshow('canny', canny)
cv.line(img,(x1,y1),(x2,y2),[255,0,0],4,lineType=cv.LINE_AA)
 
mandis=abs(x2-x1) + abs(y2-y1)
euclidean=int(math.sqrt((x2-x1)**2 + (y2-y1)**2))
text="Euclidean Distance  is "+str(euclidean) +" Manhattan Distance is "+str(mandis)
print(mandis)
cv.putText(img,text,(14,18),cv.FONT_HERSHEY_TRIPLEX,0.5,(255,255,255),1)
cv.imshow('image', img)
cv.waitKey()
