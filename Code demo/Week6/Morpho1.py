
import cv2
import numpy as np
import matplotlib.pyplot as plt
#Read the image for erosion
img1= cv2.imread("img2.jpg",0)
#Acquire size of the image
m,n= img1.shape 
#Show the image
cv2.imshow("Anh goc",img1)
# Define the structuring element
# k= 11,15,45 -Different sizes of the structuring element
k=5
SE= np.ones((k,k), dtype=np.uint8)
constant= (k-1)//2
#Define new image
imgErode= np.zeros((m,n), dtype=np.uint8)
#Erosion without using inbuilt cv2 function for morphology
for i in range(constant, m-constant):
  for j in range(constant,n-constant):
    temp= img1[i-constant:i+constant+1, j-constant:j+constant+1]
    product= temp*SE
    imgErode[i,j]= np.min(product)

# imgDilate= np.zeros((m,n), dtype=np.uint8)
# SED= np.array([[0,1,0], [1,1,1],[0,1,0]])
# constant1=1

# #Dilation
# for i in range(constant1, m-constant1):
#   for j in range(constant1,n-constant1):
#     temp= img1[i-constant1:i+constant1+1, j-constant1:j+constant1+1]
#     product= temp*SED
#     imgDilate[i,j]= np.max(product)

cv2.imshow("Opening", imgErode)
cv2.waitKey()