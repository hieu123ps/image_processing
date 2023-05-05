import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("phieu.jpg",0)
m, n = img.shape
h = np.zeros((m, n), np.uint8)
for i in range (m):
    for j in range (n):
        if(img[i][j] < 127):
            h[i][j] = 256
        else:
            h[i][j] = 0
cv2.imwrite("goc.png",h)

