import cv2 as cv #import cv2 module into my program an define the word as cv to shorten it
import sys #import sys

img = cv.imread('ZAP.png', 0) #find the image called ZAP.png in the directory and give the object to img, i set the image as grey scale(Black & White) for this exple
res = cv.resize(img,None,fx=0.5, fy=0.5, interpolation = cv.INTER_CUBIC) #resize the object to the scale factor

if img is None: #if the object is not found then run the code below
    sys.exit("The image could not be read.") # if the image could not be found let the user know
cv.imshow("OpenCV Image", img)

cv.waitKey(0) #this allows a user to terminate the program with a key entered and close the windows 
cv.destroyAllWindows()