import cv2
import matplotlib as plt
import numpy as np
#đọc và hiển thị ảnh
img = cv2.imread("pikachu.jpg")
cv2.imshow("Before",img)

#Chuyển ảnh màu thành ảnh đa mức xám

## sử dụng tham số trong hàm imread
def GR3(img):
    # • IMREAD_ANYCOLOR = 4
    # • IMREAD_ANYDEPTH = 2
    # • IMREAD_COLOR = 1
    # • IMREAD_GRAYSCALE = 0
    # • IMREAD_LOAD_GDAL = 8
    # • IMREAD_UNCHANGED = -1
    img = cv2.imread("pikachu.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("After cvt", img)

##Sử dụng công thức
def GR1(img):
    B, G, R = cv2.split(img)
    gray1 = np.uint8(R/3 + G/3 + B/3)
    cv2.imshow("RGB Image 1", gray1)

def GR2(img):
    B, G, R = cv2.split(img)
    gray2 = np.uint8(0.299*R+0.5587*G+0.114*B)
    cv2.imshow("RGB Image 2", gray2)

GR1(img)
GR2(img)
GR3(img)



cv2.waitKey(0)
cv2.destroyAllWindows()