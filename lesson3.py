"""
    Lesson 3:
        color space
        RGB, HSV, HIS...
"""

import cv2 as cv
import numpy as np

"""
    using PC camera to track green object
"""
def extrace_object_demo():
    # 0 is camera, or it can be a src of a video
    capture = cv.VideoCapture(0)  
    while(True):
        # ret to check if has return valuee
        ret, frame = capture.read()
        if not ret:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        lower_hsv = np.array([37,43,46])
        upper_hsv = np.array([77, 255, 255])
        # follow HSV table
        mask = cv.inRange(hsv, lowerb= lower_hsv, upperb=upper_hsv)

        cv.imshow("video", frame)
        cv.imshow("mask", mask)
        c = cv.waitKey(40)
        if c ==27:
            break
        

src = cv.imread("C:/Users/47902/Desktop/lena.png")
cv.namedWindow("inputimage",cv.WINDOW_AUTOSIZE)
cv.imshow("inputimage",src)

# b, g, r = cv.split(src)
# cv.imshow("blue channel", b)

# src1 = cv.merge([b,g,r])



cv.waitKey(0)
cv.destroyAllWindows()