# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2 as cv
import numpy as np

# open a video with no sound 
def video_demo():
    capture = cv.VideoCapture(0)
    # 0,1,2 is the camera of computer or it should be the src of a video 
    while(True):
        ret,frame = capture.read()
        frame = cv.flip(frame,1)
        cv.imshow("video",frame)
        c = cv.waitKey(50)
        if c == 27:
            break

#
def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    

def access_pixels(image):
    print(image.shape)
    # height, weight, channels = shape[0,1,2]
    

#
def create_img():
    img = np.zeros([400,400,3],np.uint8)        # initialize as all 0 or, np.ones intialize with all 1 
    img[ : , : , 0] = np.ones([400 , 400]) * 255  # change with one channel
    cv.imshow("new img", img)
    
    
def extrace_object_demo():
    capture = cv.VideoCapture(0)            # 0 is camera, or it can be a src of a video
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break;
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37,43,46])
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lowerb= lower_hsv, upperb=upper_hsv)
        cv.imshow("video", frame)
        cv.imshow("mask", mask)
        c = cv.waitKey(40)
        if c ==27:
            break
    

src = cv.imread("C:/Users/47902/Desktop/VISA/info.png")
cv.namedWindow("inputimage",cv.WINDOW_AUTOSIZE)
cv.imshow("inputimage",src)
create_img()
extrace_object_demo()
#get_image_info(src)
#gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)            # make the picture gray
#cv.imwrite("D:/result.png",gray)       # save it
#cv.bitwise_not(src) # inverse each pixel and it will 285 time  s faster than for *3
b, g, r = cv.split(src)
cv.imshow("blue channel", b)

src1 = cv.merge([b,g,r])
cv.waitKey(8000)
cv.destroyAllWindows()

