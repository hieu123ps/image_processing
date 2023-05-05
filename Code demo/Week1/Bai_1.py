import cv2
import numpy as np

w, h = 600, 800
start_point = (800, 0)
end_point = (0, 600)
color = [(0,0,0), (0, 255, 0), (255,0,0), (0,0,255)]
thickness = 5

def Rec(w, h, ):
    r = np.zeros(w, h, 3).astype(np.uint8)
    return cv2.rectangle(r, )

def main():
    blank_img = np.zeros((w, h, 3)).astype(np.uint8)
    print(blank_img)
    gray1 = cv2.line(blank_img, start_point, end_point, color[1], thickness)


    cv2.imshow('Gray.png', gray1)
    cv2.waitKey()
    cv2.destroyAllWindows()
    #cv2.imwrite('Gray.png', grayImg)



if __name__ == "__main__":
    main()