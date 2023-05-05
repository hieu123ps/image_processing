import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
def imhist(img):
    m,n = img.shape
    h = [0.0]*256
    for i in range (m):
        for j in range (n):
            h[img[i][j]] += 1
    return np.array(h)
def convert(img, g):
    m,n = img.shape
    g_img = np.zeros((m,n),np.uint8)
    for i in range(m):
        for j in range(n):
           g_img[i][j] = np.uint8(255*(img[i][j]/255)**g)
    return g_img


img = cv2.imread("keodan_dau.tif",0)
# cv2.imshow("anhgoc",img)
his_goc = imhist(img)
print(img.shape)
plt.plot(his_goc,'black')

g1 = convert(img,2)
# cv2.imshow("g = 3",g1) 
his1 = imhist(g1)
plt.plot(his1,'red') 

g2 = convert(img,0.3)
# cv2.imshow("g = 0.3",g2)
his2 = imhist(g2)
plt.plot(his2,'blue')

g3 = cv2.equalizeHist(img)
# cv2.imshow("g = c",g3)
his3 = imhist(g3)
plt.plot(his3,'yellow')
plt.show()
cv2.waitKey(0)