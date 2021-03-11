import cv2
import numpy as np

img=cv2.imread("C:/Users/imrk0/Desktop/CV/0_img/sample6.PNG",0)
cv2.imshow("Original",img)
img = cv2.threshold(img,0,255,cv2.THRESH_BINARY)[1]
num_labels, labels = cv2.connectedComponents(img)
x=1
a=[]
b=[]
for i in range(len(labels[0])):
    for j in range(len(labels[0])):
        if labels[i][j]==x:
            a.append(i)
            b.append(j)
            x+=1

label_hue = np.uint8(179*labels/np.max(labels))
blank_ch = 255*np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue,blank_ch,blank_ch])
labeled_img = cv2.cvtColor(labeled_img,cv2.COLOR_HSV2BGR)
labeled_img[label_hue==0] = 0
labeled_img = cv2.putText(labeled_img,"Number of components = "+str(num_labels),(5,25), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)

for i in range(x-1):
    labeled_img = cv2.putText(labeled_img,str(i),(b[i],a[i]),cv2.FONT_HERSHEY_SIMPLEX,0.4,(255,255,255),1,cv2.LINE_AA)

cv2.imshow("Labeled",labeled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()