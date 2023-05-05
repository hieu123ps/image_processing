import cv2     # Thư viện OpenCV
import numpy as np   # Thư viện numy để làm việc dữ liệu kiểu mảng
import matplotlib.pyplot as plt # import thư viện matplotlib để vẽ ảnh

# Định nghĩa hàm Tich_chap() để lọc Trung bình, Trung bình có trọng số và lọc Gaussian
def Tich_chap(img,mask):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1):
        for j in range(1, n-1):
            temp   =  img[i-1, j-1]    * mask[0, 0]\
                   +  img[i-1, j]      * mask[0, 1]\
                   +  img[i-1, j + 1]  * mask[0, 2]\
                   +  img[i, j-1]      * mask[1, 0]\
                   +  img[i, j]        * mask[1, 1]\
                   +  img[i, j + 1]    * mask[1, 2]\
                   +  img[i + 1, j-1]  * mask[2, 0]\
                   +  img[i + 1, j]    * mask[2, 1]\
                   +  img[i + 1, j + 1]* mask[2, 2]
            img_new[i, j]= abs(temp)
    img_new = img_new.astype(np.uint8)
    return img_new

#Định nghĩa toán tử SobelX (row)
SobelX = np.array(([-1,-2,-1],
                    [0, 0, 0],
                    [1, 2, 1],), dtype="float")
#Định nghĩa toán tử sobelY (col)
SobelY = np.array(([1,0,-1],
                    [2,0, -2],
                    [1, 0, -1],), dtype="float")

# Định nghĩa toán tử PrewittX
PreX = np.array(([-1, -1,-1]), dtype='float')

fig = plt.figure(figsize=(16, 9)) # Tạo vùng vẽ tỷ lệ 16:9
(ax1, ax2, ax3,ax7), (ax4, ax5, ax6,ax8) = fig.subplots(2, 4) # Tạo 6 vùng vẽ con

# Đọc và hiển thị ảnh gốc
image = cv2.imread('man_photo.png', 0)
ax1.imshow(image, cmap='gray')
ax1.set_title("Ảnh gốc")


sX = Tich_chap(image,SobelX) #Gọi hàm lọc
ax2.imshow(sX, cmap='gray')
ax2.set_title("SobelX mask")

sY = Tich_chap(image,SobelY) #Gọi hàm lọc
ax3.imshow(sY, cmap='gray')
ax3.set_title("SobelY mask")

canny = cv2.Canny(image, 50,200)
ax4.imshow(canny, cmap='gray')
ax4.set_title("Canny")

sXY = sY + sX
ax5.imshow(sXY, cmap="gray")
ax5.set_title("SobelX+SobelY")

# Hiển thị vùng vẽ
plt.show()