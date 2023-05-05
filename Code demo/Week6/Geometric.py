import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline
import cv2

a = None
if not a:
    print(True)

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

#translation
img = cv2.imread('pikachu.jpg')
rows, cols = img.shape[:2]

M = np.float32(
        [
            [1, 0, 100],
            [0, 1, 50]
        ]
)

affine_transform(img, M, cv2.INTER_LINEAR)

#rotation
h, w = img.shape[:2]

M = cv2.getRotationMatrix2D((w//2, h//2), 90, 1)
affine_transform(img, M, cv2.INTER_CUBIC)
M = cv2.getRotationMatrix2D((w//2, h//2), -90, 1)
affine_transform(img, M, cv2.INTER_CUBIC)
M = cv2.getRotationMatrix2D((w//2, h//2), 90, 0.5)
affine_transform(img, M, cv2.INTER_CUBIC)
M = cv2.getRotationMatrix2D((w//4, h//4), 90, 1)
affine_transform(img, M, cv2.INTER_CUBIC)

#Transformation matrix from points
img = cv2.imread('drawing.png')
pts1 = np.float32([[35,35],[140,50],[35,140]]) #tọa độ ban đầu
pts2 = np.float32([[10,100],[200,50],[100,250]]) #tọa đọa cần xoay

M = cv2.getAffineTransform(pts1,pts2)

print("getAffineTransform=",M)
print(img.shape)
affine_transform(img, M)

#Perspective transformation
def perspective_transform(img, tmatrix, output_size, flags=cv2.INTER_LINEAR, save_result=None):
    rows, cols, _ = img.shape
    dst = cv2.warpPerspective(img, tmatrix, output_size, flags=flags)
    if save_result:
        cv2.imwrite(save_result, dst)
        print(f"Saved output image to {save_result}")
    plt.figure(figsize=(12, 16))
    plt.subplot(1, 2, 1), plt.imshow(img[...,::-1]), plt.title("original")
    plt.subplot(1, 2, 2), plt.imshow(dst[...,::-1]), plt.title("translated")
    plt.show()
img = cv2.imread('receipt.jpg')
plt.figure(figsize=(8, 10))
plt.imshow(img[...,::-1])

pts1 = np.float32([[94, 253], [531, 93], [439,909], [903, 653]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
 
M = cv2.getPerspectiveTransform(pts1, pts2)
perspective_transform(img, M, (300, 300))
print('perspective_transform = ',M)

# Points generator
def get_grid(x, y, homogenous=False):
    coords = np.indices((x, y)).reshape(2, -1)
    return np.vstack((coords, np.ones(coords.shape[1]))) if homogenous else coords
coords = get_grid(2, 3)
print('coords = ',coords)