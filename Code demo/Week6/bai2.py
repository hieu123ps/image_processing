import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("img01.png")
h, w = img.shape[:2]
def affine_transform(img, tmatrix, flags=cv2.INTER_LINEAR, save_result=True):
    rows, cols, _ = img.shape
    dst = cv2.warpAffine(img, tmatrix, (cols, rows), flags=flags)
    if save_result:
        cv2.imwrite(save_result, dst)
        print(f"Saved output image to {save_result}")
    plt.figure(figsize=(12, 16))
    plt.subplot(1, 2, 1), plt.imshow(img[...,::-1]), plt.title("original")
    plt.subplot(1, 2, 2), plt.imshow(dst[...,::-1]), plt.title("translated")
    plt.show()


#xoay 30 
M = cv2.getRotationMatrix2D((w//2, h//2), 30, 1)
print('Ma trận xoay: ' , M.T)
affine_transform(img, M, cv2.INTER_CUBIC, 'Rout30.png')

#tăng kích thước x2
M = cv2.getRotationMatrix2D((w//2, h//2), 0, 2)
print('Ma trận tăng x2: ' , M.T)
affine_transform(img, M, cv2.INTER_CUBIC, 'X2image.png')

