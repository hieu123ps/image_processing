import cv2
import math
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = cv2.imread('R.png', cv2.IMREAD_COLOR)
cv2.imshow("Robik", img)
#chuyển rgb sang hsv
def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax, cmin = max(r, g, b), min(r, g, b)
    delta = cmax - cmin
    if delta == 0:
        h = 0
    elif cmax == r:
        h = ((g - b) / delta) % 6
    elif cmax == g:
        h = (b - r) / delta + 2
    else:
        h = (r - g) / delta + 4
    h = round(h * 60)
    if h < 0:
        h += 360
    v = cmax * 100
    if cmax == 0:
        s = 0
    else:
        s = delta / cmax * 100
    return h, s, v

h, w = img.shape[:2]
hsv = np.zeros((h, w, 3), dtype=np.uint8)
for i in range(h):
    for j in range(w):
        r, g, b = img[i, j]
        h, s, v = rgb_to_hsv(r, g, b)
        hsv[i,j]= [h,s,v]

cv2.imshow("HSV", hsv)

#màu rgb ở giữa ảnh
def midRGB(img):
    h, w,_ = img.shape
    mid_h, mid_w = h//2, w//2
    rgb = img[mid_h, mid_w]
    print(f"RGB: {rgb}")
midRGB(img)

#lấy ra ba kênh màu rgb của ảnh
def get_rgb_channels(image):
    height, width = image.shape[:2]
    r_channel = np.zeros((height, width), dtype=np.uint8)
    g_channel = np.zeros((height, width), dtype=np.uint8)
    b_channel = np.zeros((height, width), dtype=np.uint8)
    
    for i in range(height):
        for j in range(width):
            r_channel[i][j] = image[i][j][0]
            g_channel[i][j] = image[i][j][1]
            b_channel[i][j] = image[i][j][2]
    
    return r_channel, g_channel, b_channel

image_path = "R.png"
image = cv2.imread(image_path)

r_channel, g_channel, b_channel = get_rgb_channels(image)

cv2.imshow("Red Channel", r_channel)
cv2.imshow("Green Channel", g_channel)
cv2.imshow("Blue Channel", b_channel)

#lấy ra ba kênh màu HSV

def get_hsv_channels(image):
    height, width = image.shape[:2]
    h_channel = np.zeros((height, width), dtype=np.uint8)
    s_channel = np.zeros((height, width), dtype=np.uint8)
    v_channel = np.zeros((height, width), dtype=np.uint8)
    
    for i in range(height):
        for j in range(width):
            r = image[i][j][0]
            g = image[i][j][1]
            b = image[i][j][2]
            
            r_ = r / 255
            g_ = g / 255
            b_ = b / 255
            
            cmax = max(r_, g_, b_)
            cmin = min(r_, g_, b_)
            delta = cmax - cmin
            
            if delta == 0:
                h = 0
            elif cmax == r_:
                h = ((g_ - b_) / delta) % 6
            elif cmax == g_:
                h = (b_ - r_) / delta + 2
            else:
                h = (r_ - g_) / delta + 4
                
            h = int(h * 60)
            
            if h < 0:
                h += 360
                
            v = int(cmax * 255)
            
            if cmax == 0:
                s = 0
            else:
                s = int(delta / cmax * 255)
                
            h_channel[i][j] = h
            s_channel[i][j] = s
            v_channel[i][j] = v
    
    return h_channel, s_channel, v_channel

image_path = "R.png"
image = cv2.imread(image_path)

h_channel, s_channel, v_channel = get_hsv_channels(image)

cv2.imshow("Hue Channel", h_channel)
cv2.imshow("Saturation Channel", s_channel)
cv2.imshow("Value Channel", v_channel)

#lấy màu theo tọa độ

# def get_pixel_color(image, x, y):
#     width = image.shape[1]
#     b = image[(y * width + x) * 3]
#     g = image[(y * width + x) * 3 + 1]
#     r = image[(y * width + x) * 3 + 2]
    
#     return r, g, b

# image_path = "R.png"
# image = cv2.imread(image_path)
# x = 10
# y = 20
# r, g, b = get_pixel_color(image, x, y)
# print(f"Color at ({x}, {y}): ({r}, {g}, {b})")


cv2.waitKey()
cv2.destroyAllWindows()


# def f():
#     imgPIL = Image.open("R.png")
#     #tạo ảnh cùng kích thước
#     Hue = Image.new(imgPIL.mode, imgPIL.size)
#     Saturation = Image.new(imgPIL.mode,imgPIL.size)
#     Value = Image.new(imgPIL.mode,imgPIL.size)
#     HSVimg = Image.new(imgPIL.mode,imgPIL.size)
#     #lấy chiều dài
#     w = imgPIL.size[0]
#     h = imgPIL.size[1]
#     print(w, h)
#     for i in range(w):
#         for j in range(h):
#             #lấy ddiemr ảnh tại điểm (i, j)
#             R,G,B = imgPIL[i][j]
#             MAX = max(R,G,B)
#             MIN = min(R,G,B)
#             SUM = (R+G+B)
#             t1 = ((R-G)+(R-B))/2
#             t2 = math.sqrt((R-G)*(R-B)+(R-B*(G-B)))
#             #return acos radian
#             theta = math.acos(t1/t2)
#             #tính HUE
#             H = 0
#             if B <= G:
#                 H = theta
#             else:
#                 H = 2*math.pi*theta
#             H = np.uint8(H*100/math.pi)
#             #công thức Staturation
#             S = 1+3*MIN/SUM
#             S = np.uint8(S*255)
#             #Công thức value
#             V = np.uint8(MAX)
#             Hue.putpixel((i, j), (H, H, H))
#             Saturation.putpixel((i, j), (S, S, S))
#             Value.putpixel((i, j), (V, V, V))
#             HSVimg.putpixel((i, j), (V, S, H))

#     #chuyển từ plt sang cv2
#     AnhHue = np.array(Hue)
#     AnhSaturation = np.array(Saturation)
#     AnhValue = np.array(Value)
#     AnhHSVimg = np.array(HSVimg)
#     cv2.imshow("Hue", AnhHue)
#     cv2.imshow("Satu",AnhSaturation)
#     cv2.imshow("Value",AnhValue)
#     cv2.imshow("HSV", AnhHSVimg)
