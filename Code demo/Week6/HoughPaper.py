import cv2     # Thư viện OpenCV
import numpy as np   # Thư viện numy để làm việc dữ liệu kiểu mảng
import matplotlib.pyplot as plt  # import thư viện matplotlib để vẽ ảnh
import math

IMG_LOCATION = 'A4.jpg'

fig = plt.figure(figsize=(16, 9))  # Tạo vùng vẽ tỷ lệ 16:9
(ax1, ax2, ax3), (ax4, ax5, ax6) = fig.subplots(2, 3)  # type: ignore # Tạo 6 vùng vẽ con

# Đọc và hiển thị ảnh gốc
image = cv2.imread(IMG_LOCATION, 0)
ax1.imshow(image, cmap='gray')
ax1.set_title("Anh goc")


edges = cv2.Canny(image, 100, 200)
ax2.imshow(edges, cmap='gray')
ax2.set_title("Canny")


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


# Hough Line P
linesP = cv2.HoughLinesP(edges, 1, np.pi / 180, 1)
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]),(0, 0, 255), 3, cv2.LINE_AA)
# ax4.imshow(cdstP, cmap='gray')
# ax4.set_title('Line')
#Coner detection
corner = cv2.cornerHarris(edges, 5, 3, 0) #thuật toán dò góc
corner = cv2.dilate(corner, None) #loại bỏ đường thẳng

cornerCordinate = cv2.goodFeaturesToTrack(image, 4, 0.05, 10)

print(cornerCordinate)
print('Kích thước ảnh = ',image.shape)
pts1 = cornerCordinate# type: ignore
print(pts1.T)
pts2 = np.float32([[0, 0],[194, 0],[0, 259],[194, 259]]) # type: ignore
M = cv2.getPerspectiveTransform(pts1,pts2)

scan = cv2.warpPerspective(image, M, (194, 259))
ax4.imsow(scan,  cmap='gray')
ax3.imshow(cdst, cmap='gray')
ax3.set_title('Hough Line')

ax5.imshow(corner, cmap='gray')
ax5.set_title('Corner')

ax6.imshow(cdstP, cmap='gray')
ax6.set_title('Hough Line P')

# ax4.axis('off')

plt.show()
cv2.waitKey(0)