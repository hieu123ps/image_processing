import cv2
import numpy as np
import matplotlib.pyplot as plt
import cv2
import numpy as np
import matplotlib.pyplot as plt

# image1 = cv2.imread("src.png", 0)
# image2 = cv2.imread("Images/Anh5.jpg", 0)
image3 = cv2.imread("src.png", 0)

kernel1 = np.ones((5,5),np.uint8)
kernel2 = np.ones((1, 20), np.uint8)


fig = plt.figure(figsize=(16, 9))  # Tạo vùng vẽ tỷ lệ 16:9
(ax1, ax2, ax3), (ax4, ax5, ax6) = fig.subplots(2, 3)  # type: ignore # Tạo 6 vùng vẽ con

# ax1.imshow(image1, cmap='gray')
# ax1.set_title("Anh goc 1 ")

# ax4.imshow(image2, cmap='gray')
# ax4.set_title("Anh goc 2")

ax3.imshow(image3, cmap='gray')
ax3.set_title("Anh goc 3")

# opening = cv2.morphologyEx(image1, cv2.MORPH_OPEN, kernel1)
# ax2.imshow(opening, cmap='gray')
# ax2.set_title("After 1")

# closing = cv2.morphologyEx(image2, cv2.MORPH_CLOSE, kernel1)
# ax5.imshow(closing, cmap='gray')
# ax5.set_title("After 2")

# Apply adaptiveThreshold at the bitwise_not of gray
image3 = cv2.bitwise_not(image3)
image3 = cv2.adaptiveThreshold(image3, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)

# Create the images that will use to extract the horizontal and vertical lines
# horizontal = np.copy(image3)

# # Specify size on horizontal axis
# cols = horizontal.shape[1]
# horizontal_size = cols // 30
# # Create structure element for extracting horizontal lines through morphology operations
# horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))

# Apply morphology operations
image3 = cv2.erode(image3, kernel2)
image3 = cv2.dilate(image3, kernel2)

ax6.imshow(image3, cmap='gray')
ax6.set_title("After 3")

plt.show()
cv2.waitKey(0)
# cv2.imwrite("Eroded3.png", imgErode)