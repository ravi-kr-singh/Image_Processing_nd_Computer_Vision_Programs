import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt  
image = cv.imread('C:/Users/imrk0/Desktop/Github/Image_Processing_nd_Computer_Vision_Programs/00_img/flower.PNG',1)
RGB_img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
# Gaussian Blur 
Gaussian = cv.GaussianBlur(image.copy(), (7, 7), 0)
RGB_gaussian = cv.cvtColor(Gaussian, cv.COLOR_BGR2RGB) 
images=[RGB_img,RGB_gaussian]
title=["original","Gaussian"]
for i in range(2):
   plt.subplot(1,2,i+1)
   plt.title(title[i])
   plt.imshow(images[i],cmap="gray")     
plt.show()
