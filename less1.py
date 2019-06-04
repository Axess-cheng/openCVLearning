# -*- coding: utf-8 -*-
"""
used Spyder Editor

now is in vscode and can been seen on git
https://github.com/Axess-cheng/openCVLearning.git


Lesson 1:
    input image and get its info
    input video

"""



import cv2 as cv
import numpy as np


# print info of image
def get_image_info(image):
    # type of input
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)


# open a video with no sound 
def video_demo():
    capture = cv.VideoCapture(0)
    # 0,1,2 is the camera of computer or it should be the src of a video 
    while(True):
        ret,frame = capture.read()
        # mirror transformation
        frame = cv.flip(frame,1)

        # show each frame
        cv.imshow("video",frame)

        c = cv.waitKey(50)
        # esc is 27 and press esc to exit
        if c == 27:
            break

    
    

    

src = cv.imread("C:/Users/47902/Desktop/lena.png")
cv.namedWindow("inputimage",cv.WINDOW_AUTOSIZE)
cv.imshow("inputimage",src)
get_image_info(src)
cv.waitKey(0)
cv.destroyAllWindows()
