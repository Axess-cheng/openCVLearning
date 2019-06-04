
"""
    FYP: Image Recognition: translate pictures of directed graphs to textual representations --Patrick Totzke
    Detecting Circles in Images using OpenCV and Hough Circles
    https://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/
"""


# import the necessary packages
# parsing command line arguments
import numpy as np
import argparse     
import cv2

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True, help = "Path to the image")
# args = vars(ap.parse_args())

# load the image, clone it for output, and then convert it to grayscale
# houghCircle nned  8-bit, single channel image
# image = cv2.imread(args["image"])
image = cv2.imread("images/8circles.png")
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.cv.CV_HOUGH_GRADIENT -> cv2.HOUGH_GRADIENT
# the CV_ prefix has been removed with opencv3, and all constants are in the cv2 submodule now
# https://answers.opencv.org/question/177506/cv2-has-no-attribute-cv_hough_gradient/
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 40)
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
 
	# show the output image
    cv2.imshow("output", np.hstack([image, output]))
    cv2.waitKey(0)