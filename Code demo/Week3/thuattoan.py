
import numpy as np
import cv2
import matplotlib.pyplot as plt

def imhist(im):
	m, n = im.shape
	h = [0.0] * 256
	for i in range(m):
		for j in range(n):
			h[im[i, j]]+=1
	return np.array(h)/(m*n)

def cumsum(h): 
    cumsum_h=[0.0]*256
    cumsum_h[0]=h[0]
    for i in range(255):
        cumsum_h[i+1]=cumsum_h[i]+h[i]
    return cumsum_h

def histeq(im):
	h = imhist(im)
	cdf = np.array(cumsum(h)) 
	sk = np.uint8(255 * cdf) 
	Y = np.zeros(im.shape,np.uint8)
	for i in range(im.shape[0]):
		for j in range(im.shape[1]):
			Y[i, j] = sk[im[i, j]]
	return Y


def main():
	im = cv2.imread("sanbay.tif",0)
	g1 = imhist(im)
	cv2.imshow("Anh goc", im)
	plt.plot(g1, "red")
	g2 = histeq(im)
	plt.plot(g2, "green")
	cv2.imshow("Sau xu li", g1)
	plt.show()
	cv2.waitKey(0)

if __name__ == "__main__":
	main()
