import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("sanbay.tif", 0)
# cv2.imshow("Before", img)

##Thủ công
def getHist(img):
    m, n = img.shape
    his = [0.0]*256
    for i in range(m):
        for j in range(n):
            his[img[i, j]] +=1
    h1 = his
    plt.plot(h1, "red")

##sử dụng hàm calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
#images -> uint8 hoặc float3 -> nên ép thành mảng
#channels -> [0] nếu là ảnh xám
#mask -> xác định vị trí muốn tính toán
#histsize -> khoảng giá trị đếm
#range -> khoảng mức xám
def calcHist(img):
    h2 = cv2.calcHist([img], [0], None, [256], [0,256])
    plt.plot(h2, "green")

getHist(img)
calcHist(img)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()