import cv2 
from matplotlib import pyplot as plt
 
img = cv2.imread("C:/Users/imrk0/Desktop/CV/00_img/random.PNG",0) 
cv2.imshow('Original', img)
plot1 = plt.figure("Original")
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.xlabel('Pixel values')
plt.ylabel('No. of pixels')
 
eq=cv2.equalizeHist(img)
cv2.imshow('changed', eq) 
plot2 = plt.figure("Changed")
plt.hist(eq.flatten(),256,[0,256], color = 'b')
plt.xlim([0,256])
plt.xlabel('Pixel values')
plt.ylabel('No. of pixels')
plt.show()
