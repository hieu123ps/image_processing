import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def affine_transform(img, tmatrix, flags=cv2.INTER_LINEAR, save_result=None):
    rows, cols, _ = img.shape
    dst = cv2.warpAffine(img, tmatrix, (cols, rows), flags=flags)
    if save_result:
        cv2.imwrite(save_result, dst)
        print(f"Saved output image to {save_result}")
    plt.figure(figsize=(12, 16))
    plt.subplot(1, 2, 1), plt.imshow(img[...,::-1]), plt.title("original")
    plt.subplot(1, 2, 2), plt.imshow(dst[...,::-1]), plt.title("translated")
    plt.show()
    
image = cv2.imread("A4.jpg")
cv2.imshow("Ảnh gốc", image)
edges = cv2.Canny(image, 100, 200)

cdst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
cdstP = np.copy(cdst)

# Hough Line
lines = cv2.HoughLines(edges, 1, np.pi/180, 250)
if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv2.line(cdst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

corner = cv2.cornerHarris(edges, 5, 3, 0) #thuật toán dò góc
corner = cv2.dilate(corner, None) #loại bỏ đường thẳng

cornerCordinate = cv2.goodFeaturesToTrack(image, 4, 0.05, 10)
cornerCordinate = np.uint8(cornerCordinate)
print(cornerCordinate)




