import cv2
import numpy as np
import matplotlib.pyplot as plt
def imhist(img):
    d, r = img.shape
    h = [0.0]*256
    for i in range (d):
        for j in range (r):
            h[img[i][j]] += 1
    return np.array(h)
def convert(img, g):
    d,r = img.shape
    g_img = np.zeros((d,r),np.uint8)
    for i in range(d):
        for j in range(r):
           g_img[i][j] = np.uint8(255*(img[i][j]/255)**g)
    return g_img 
img = cv2.imread('sanbay.tif',0)
cv2.imshow("anh_goc,", img)
his_goc = imhist(img)
print(img.shape)
plt.plot(his_goc,'black')

anhsau = convert(img,3)
cv2.imshow("anh_sau",anhsau) 
his_sau = imhist(anhsau)
plt.plot(his_sau,'black') 

plt.show()
cv2.waitKey(0)