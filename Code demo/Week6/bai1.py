import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("img01.png")
img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

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

edges = cv2.Canny(img, 100,200)

lines = cv2.HoughLinesP(
    edges,  # Input edge image
    1,  # Distance resolution in pixels
    np.pi / 170,  # Angle resolution in radians
    threshold=50,  # Min number of votes for valid line
    minLineLength=5,  # Min allowed length of line
    maxLineGap=50  # Max allowed gap between line for joining them
)

lines_list = []
print('Line = ',lines)
for points in lines:
    x1, y1, x2, y2 = points[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 255), 2)
    print('Line=',points[0])
    lines_list.append([(x1, y1), (x2, y2)])
plt.figure(figsize=(12, 16))
plt.imshow(img), plt.title("original")
plt.show()
cv2.imshow("Đặc trưng ảnh", edges)
cv2.imshow("Vẽ đường viền",image)
cv2.waitKey(0)