#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ADMIN
#
# Created:     07/02/2023
# Copyright:   (c) ADMIN 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cv2
import numpy as np
import matplotlib.pyplot as plt

def gramImg(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)

def imhist(im):
    m, n = im.shape
    h = [0, 0]*256
    for i in range(m):
        for j in range(n):
            h[im[i, j]] += 1
    return np.array(h)/(m*n)

def main():
    img = cv2.imread('keodan_dau.tif', 0)
    cv2.imshow("ANH GOC", img)
    g = gramImg(img, 3)
    cv2.imshow('ANH 1', g)
    his_goc = imhist(img)
    plt.plot(his_goc, 'red')
    plt.show()
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
