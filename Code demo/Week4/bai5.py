import cv2
import numpy as np
import matplotlib.pyplot as plt

def transWtoB(im):
    m, n = im.shape
    h = np.array(im)
    for i in range(m):
        for j in range(n):
            if (h[i][j] <= 172):
                h[i][j] = 255
            else:
                h[i][j] = 0
    return h

def imhist(im): #đọc histogram
    m, n = im.shape
    h = np.zeros((m*n), np.uint8)
    for i in range(m):  
        for j in range(n):
            h[im[i,j]] += 1
    return np.array(h)

def main():
    img = cv2.imread("phieu.jpg", 0)
    g1 = imhist(img)
    m = transWtoB(img)
    cv2.imwrite("hii.png", m)
    cv2.imshow("a=g1", img)
    cv2.imshow("gedge", m)
    plt.plot(g1, "blue")
    plt.show()
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()