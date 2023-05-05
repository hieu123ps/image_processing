import cv2
import numpy as np
import matplotlib.pyplot as plt

f = np.ones((5,5),np.float32)/25

def tich_chap(im):
    m, n = im.shape
    h = np.zeros((m,n),np.uint8)
    for i in range(1, m-1):
        for j in range(1, n-1):
            temp += 1
            h[i,j] = temp
    return h


def main():
    img = cv2.imread("noisy_image.tif")
   


if __name__ == "__main__":  
    main()