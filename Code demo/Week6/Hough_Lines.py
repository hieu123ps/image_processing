import sys
import math
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(16, 9)) # Tạo vùng vẽ tỷ lệ 16:9
(ax1, ax2, ax3), (ax4, ax5, ax6) = fig.subplots(2, 3) # Tạo 6 vùng vẽ con


def main(argv):
    
    default_file = 'sudoku.png'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_lines.py [image_name -- default ' + default_file + '] \n')
        return -1
    

    dst = cv.Canny(src, 50, 200, None, 3)
    
    # Copy edges to the images that will display the results in BGR
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)    

    lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
    A = []
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
            print(rho, theta)
            cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)

    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)

    ax1.imshow(src,  cmap='gray')
    ax2.imshow(cdst,  cmap='gray')
    ax3.imshow( cdstP,  cmap='gray')

    # cv.imshow("Source", src)
    # cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    # cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
    plt.show()
    cv.waitKey()
    return 0
    
if __name__ == "__main__":
    main(sys.argv[1:])

'''
Hàm HoughLines() phải tính toán quá nhiều để tìm đường thẳng, còn Probabilistic Hough ít tính toán hơn. Nó không kiểm tra tất cả các pixel mà chỉ lấy 1 số cụm pixel vừa đủ để tìm ra đường thẳng.

Nhược điểm thứ 2 là HoughLines() không xác định được điểm đầu và điểm cuối của đoạn thẳng. Do đó chúng ta dùng HoughLinesP() để khắc phục nhược điểm

Thuật toán này có thêm 2 tham số nữa:

minLineLength – Độ dài tối thiểu của đường thẳng
maxLineGap – Nếu 2 đường thẳng có khoảng đứt gãy ở giữa ngắn hơn maxLineGap thì được xem là 1 đường thẳng
'''