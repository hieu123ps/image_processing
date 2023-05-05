import cv2
import numpy as np
import matplotlib.pyplot as plt
 
img = cv2.imread("keodan_dau.tif", 0)
cv2.imshow("G", img)

##Hiển thị hist
def getHist(img):
    m, n = img.shape
    his = [0.0]*256
    for i in range(m):
        for j in range(n):
            his[img[i, j]] +=1
    return np.array(his)

##Biến đổi gamma
def GammaHist(img, g):
    m, n = img.shape
    g_img = np.zeros((m,n),np.uint8)
    for i in range(m):
        for j in range(n):
           g_img[i][j] = np.uint8(255*(img[i][j]/255)**g)
    return g_img 

##Biến đổi từng phần
def SplitHist(img):
    m,n =img.shape
    r = [0]*256
    h = [0.0]*256
    #tính h(r)
    for i in range(m):
        for j in range(n):
            h[img[i,j]]+=1
            if img[i,j] not in r:
                r.append(img[i,j])
    #tính p(r)
    p = [0.0]*256
    for i in range(len(r)):
        p[i] = r[i]/(m*n)
    s = []


g1 = GammaHist(img, 1.5)
cv2.imshow("G1", g1)

cv2.waitKey()
cv2.destroyAllWindows()