import cv2 
from matplotlib import pyplot as plt
import matplotlib.cm as cm


img = cv2.imread("C:/Users/imrk0/Desktop/CV/0_img/img4.jpg",0) 
original_img = cv2.imread("C:/Users/imrk0/Desktop/CV/0_img/img4.jpg",1)
original_img = cv2.cvtColor(original_img,cv2.COLOR_BGR2RGB)

plot1 = plt.figure("Histogram of Original Image")
plt.hist(img.flatten(),256,[0,256], color = 'b')
plt.xlim([0,256])
plt.xlabel('Pixel values')
plt.ylabel('No. of pixels')

t=155

x,y= img.shape[:2]
for i in range(x):
    for j in range(y):
        if(img[i,j]<t):  
            img[i,j]=70
        else: 
            img[i,j]=210

plot2 = plt.figure("Original Image")
plt.imshow(original_img)

plot3 = plt.figure("Segmented image : ")
plt.imshow(img,cmap=cm.gray)

plot4 = plt.figure("Histogram of Segmented Image")
plt.hist(img.flatten(),256,[0,256], color = 'b')
plt.xlim([0,256])
plt.xlabel('Pixel values')
plt.ylabel('No. of pixels')

plt.show()

