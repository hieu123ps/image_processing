import cv2
import numpy as np
import matplotlib.pyplot as plt
img_new= cv2.imread("img1.jpg",0)
cv2.imshow("Anh goc",  img_new)
p, q = img_new.shape
imgDilate= np.zeros((p,q), dtype=np.uint8)
SED= np.array([[0,1,0], [1,1,1],[0,1,0]])
constant1=1

#Dilation
for i in range(constant1, p-constant1):
  for j in range(constant1,q-constant1):
    temp= img_new[i-constant1:i+constant1+1, j-constant1:j+constant1+1]
    product= temp*SED
    imgDilate[i,j]= np.max(product)

plt.imshow(imgDilate,cmap="gray")
cv2.imshow("Dilated", imgDilate)
cv2.waitKey()