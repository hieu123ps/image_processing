import cv2
import numpy as np  
import matplotlib.pyplot as plt

def imhist(im): #đọc histogram
    m, n = im.shape
    h = [0.0]*256
    for i in range(m):  
        for j in range(n):
            h[im[i,j]] += 1
    return np.array(h)

def fixedHist(im, g): #sửa histogram theo chỉ số g
    m, n = im.shape
    r = np.zeros((m, n), np.uint8)
    for i in range(m):
        for j in range(n):
            r[i, j] = np.uint8(255*(im[i, j]/255)**g)
    return r


def main():
    a1 = cv2.imread("xuongsong.tif", 0)
    g1 = imhist(a1)
    cv2.imshow("Before", a1)
    plt.plot(g1, 'red')
    g2 = fixedHist(a1, 0.5)
    cv2.imshow("After",g2)
    plt.plot(g2, 'blue')
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()