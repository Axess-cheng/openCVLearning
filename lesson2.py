
"""
    Lesson 2:
        numpy operation for array
        operation in pixels
"""

import cv2 as cv
import numpy as np

def access_pixels(image):
    print(image.shape)
    # height, width, channels = shape[0,1,2]
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("height : %s, width : %s, channels : %s"%(height, width, channels))
    for row in range(height):
        for col in range(width):
            for chan in range(channels):
                pv = image[row, col, chan]
                image[row,col,chan] = 255 - pv

    # inverse each pixel and it will 285 time  s faster than for *3
    #cv.bitwise_not(src)

    cv.imshow("pixels_demo", image)



"""
    this image are "BGR" blue, green, red
    0 is white; 255 is black
"""
def create_img():
    # initialize as all 0 or
    # np.ones intialize with all 1 
    img = np.zeros([400,400,3],np.uint8)        

    # change one channel, first channel are alll 255, so its a blue image
    img[ : , : , 0] = np.ones([400 , 400]) *255
    cv.imshow("new img", img)

create_img()
src = cv.imread("C:/Users/47902/Desktop/lena.png")
cv.namedWindow("inputimage",cv.WINDOW_AUTOSIZE)
cv.imshow("inputimage",src)
t1 = cv.getTickCount()
access_pixels(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()*1000
print("time : %s ms"%(time))
cv.waitKey(0)
cv.destroyAllWindows()

# another function to test time 
# timeit