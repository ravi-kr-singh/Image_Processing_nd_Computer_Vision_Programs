import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def global_thresholding(img):    
    x,y= img.shape[:2]
    sum = 0
    count = 0
    for i in range(x):
        for j in range(y):
            sum = sum + img[i,j]
            count = count + 1

    Mean = int(sum/count)        
    return Mean
    

img = cv2.imread("C:/Users/imrk0/Desktop/CV/0_img/img14.png")

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
orignal_img = img
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
img = cv2.resize(gray,(850,1179))

x,y=img.shape

th1= global_thresholding(img[0:int(x/2), 0:int(y/2)])
th2= global_thresholding(img[0:int(x/2), int(y/2):y])
th3= global_thresholding(img[int(x/2):x, 0:int(y/2)])
th4= global_thresholding(img[int(x/2):x, int(y/2):y])

print("Threshold values for 4 subregions are- ",th1," ",th2," ",th3," ",th4)

ret1, img[0:int(x/2), 0:int(y/2)] = cv2.threshold(img[0:int(x/2), 0:int(y/2)], th1, 255, cv2.THRESH_BINARY)
ret1, img[0:int(x/2), int(y/2):y] = cv2.threshold(img[0:int(x/2), int(y/2):y], th2, 255, cv2.THRESH_BINARY)
ret1, img[int(x/2):x, 0:int(y/2)] = cv2.threshold(img[int(x/2):x, 0:int(y/2)], th3, 255, cv2.THRESH_BINARY)
ret1, img[int(x/2):x, int(y/2):y] = cv2.threshold(img[int(x/2):x, int(y/2):y], th4, 255, cv2.THRESH_BINARY)

plot1 = plt.figure("Original")
plt.imshow(orignal_img)
plot2 = plt.figure("Segmented image : ")
plt.imshow(img,cmap=cm.gray)
plt.show()