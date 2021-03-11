import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("C:/Users/imrk0/Desktop/Github/Image_Processing_nd_Computer_Vision_Programs/00_img/sample_2.jpg",1)
RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
RGB_dst = cv.cvtColor(dst, cv.COLOR_BGR2RGB)
plot1 = plt.figure("Original")
plt.imshow(RGB_img)
plot2 = plt.figure("After Noise reduction ")
plt.imshow(RGB_dst)
plt.show()