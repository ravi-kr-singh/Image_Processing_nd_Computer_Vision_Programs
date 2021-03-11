import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('C:/Users/imrk0/Desktop/CV/00_img/leaf.jpg',cv2.IMREAD_GRAYSCALE)
original_img = cv2.imread('C:/Users/imrk0/Desktop/CV/00_img/leaf.jpg',cv2.IMREAD_COLOR)
original_img_copy = original_img.copy()
 
kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
for i in range(len(img)):
    for j in range(len(img[0])):
        if(img[i][j]==255):  img[i][j]=1
        else: img[i][j]=10
        
dst = cv2.filter2D(img,-1,kernel)
#print(dst)
 
for i in range(dst.shape[0]):
  #if(max(dst[i]>10)): print(max(dst[i]))  
  for j in range(dst.shape[1]):
    if dst[i,j] >=72:
      x = i-2
      y = j-2
      for a in range(5):
        for b in range(5):
          original_img[x,y] = 0
          x = x+1
        y = y+1
        x = i-2
        
      
RGB_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
RGB_original = cv2.cvtColor(original_img_copy, cv2.COLOR_BGR2RGB)    
 
plot1 = plt.figure("Original Image")
plt.imshow(RGB_original)
plot2 = plt.figure("Point extraction")
plt.imshow(RGB_img)
plt.show()
