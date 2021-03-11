import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt  
 
 
image = cv.imread("C:/Users/imrk0/Desktop/Github/Image_Processing_nd_Computer_Vision_Programs/00_img/board.png",1)
cann=cv.Canny(image,200,400)
 
 
x=cv.Sobel(cann,cv.CV_64F,1,0,ksize=5)
y=cv.Sobel(cann,cv.CV_64F,0,1,ksize=5)
 
 
imgy_float32 = np.float32(y)
imgx_float32 = np.float32(x)
sobely = cv.cvtColor(imgy_float32,cv.COLOR_GRAY2BGR)
sobelx =cv.cvtColor(imgx_float32,cv.COLOR_GRAY2BGR)
 
 
sobelxy=cv.bitwise_or(sobelx,sobely)
Titles =["original","sobel-y","sobel-x","sobel-xy","canny"] 
images =[image, sobelx, sobely,sobelxy,cann] 
count = 5
  
 
for i in range(count): 
    plt.subplot(2, 3, i + 1) 
    plt.title(Titles[i]) 
    plt.imshow(images[i],cmap="gray") 
  
plt.show()
