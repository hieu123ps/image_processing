import cv2
import matplotlib.pyplot as plt
import numpy as np

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

#Doc va hien thi anh
img = cv2.imread('demo.png', 1)
cv2.imshow("Show Image", img)

#Xu li ba kenh mau --> anh xam
B, G, R = cv2.split(img)
gray1 = np.uint8(R/3 + G/3 + B/3)
cv2.imshow("RGB Image 1", gray1)

#Anh da muc xam
gray2 = np.uint8(0.299*R+0.5587*G+0.114*B)
cv2.imshow("RGB Image 2", gray2)


g2 = convert(gray2,2)
cv2.imshow("g = 0.3",g2)
his2 = imhist(g2)
cv2.imwrite("final.jpg",his2)

#Hien thi khung hinh
cv2.waitKey()
cv2.destroyAllWindows()