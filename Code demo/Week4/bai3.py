import cv2
import numpy as np
import matplotlib.pyplot as plt

def mihist(im):
    m, n = im.shape
    h = np.zeros((m, n), np.uint8)
    for i in range(m):
        for j in range(n):
            h[im[j, i]] +=1
    return np.array(h)

def binary_hist(im):
    pass

def main():
    g1 = cv2.imread("keodan_dau.tif", 0)
    g2 = mihist(g1)
    plt.plot(g1, "red")
    plt.show()
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":  
    main()