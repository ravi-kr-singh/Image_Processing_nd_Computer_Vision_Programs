import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def iterative_algorithm(img):
    img_array = np.array(img).astype(np.float32)
    I=img_array
    Ti=50 #Set initial arbitrary value as threshold value
    b=1
    m,n=I.shape
    diff = 255
    count = 1
    while diff!=0:
        foreground=0
        background=0
        sum_fg=0
        sum_bg=0
        for i in range(1,m):
             for j in range(1,n):
                tmp=I[i][j]
                if tmp>=Ti:
                    foreground = foreground + 1
                    sum_fg= sum_fg + int(tmp) 
                else:
                    background = background + 1
                    sum_bg = sum_bg + int(tmp)
        
        mean_fg = int(sum_fg/foreground)
        mean_bg = int(sum_bg/background)
        mean = int((mean_bg+mean_fg)/2)
        diff = abs(mean - Ti)
        Ti=mean
        print("Iteration " + str(count) + " Threshold value : " + str(Ti))
        count = count + 1
    
    return Ti
        
    

img = cv2.imread("C:/Users/imrk0/Desktop/CV/0_img/img10.jpg")

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
orignal_img = img
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
img = cv2.resize(gray,(1017,1199))

final_threshold_value = iterative_algorithm(img)
print("Final Threshold value : " + str(final_threshold_value))
ret1, th1 = cv2.threshold(img, final_threshold_value, 255, cv2.THRESH_BINARY)
plot1 = plt.figure("Original")
plt.imshow(orignal_img)
plot2 = plt.figure("Segmented image : ")
plt.imshow(th1,cmap=cm.gray)
plt.show()

