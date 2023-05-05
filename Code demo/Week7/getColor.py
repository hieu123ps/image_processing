import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('R.png', cv2.IMREAD_COLOR)
#tìm ra RGB, HSV của 1 điểm ảnh bất kỳ
R,G,B = img.split()
print(R, G, B)