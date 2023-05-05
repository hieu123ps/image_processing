import cv2
import numpy as np
import matplotlib.pyplot as plt

def convert(im):
    m, n = im.shape
    h = [0.0]*256
    for i in range(m):
        for j in range(n):  
            h[im[i,j]] += 1
    return np.array(h)

def main():
    g1 = cv2.imread("keodan_dau.tif", 0)
    plt.plot(convert(g1), "yellow")
    g2 = cv2.imread("xuongsong.tif", 0)
    plt.plot(convert(g2), "blue")
    g3 = cv2.imread("sanbay.tif", 0)
    plt.plot(convert(g3), "green")
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()