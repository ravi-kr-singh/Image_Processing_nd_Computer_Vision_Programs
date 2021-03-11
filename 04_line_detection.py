import cv2
import numpy as np
from matplotlib import cm, pyplot as plt

square=cv2.imread('C:/Users/imrk0/Desktop/CV/00_img/bridge2.jpg')

v = np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]])
h = np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
sf = np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]])
sb = np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
dst1 = cv2.filter2D(square,0,v)
dst2 = cv2.filter2D(square,0,h)
dst3 = cv2.filter2D(square,0,sf)
dst4 = cv2.filter2D(square,0,sb)

plot1 = plt.figure("Original")
plt.imshow(square)
plot2 = plt.figure("Vertical")
plt.imshow(dst1)
plot3 = plt.figure("Horizontal")
plt.imshow(dst2)
plot4 = plt.figure("Slant Forward")
plt.imshow(dst3)
plot5 = plt.figure("Slant Backward")
plt.imshow(dst4)
plt.show()