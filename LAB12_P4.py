import cv2 as cv # we are importing cv2 as cv to shorten it out
import numpy as np # we are also importing numpy as np to shorten ut up

img = cv.imread('MRGOPHER.jpeg') #here we are creating a object called img that is associated with the jpg used
res = cv.resize(img,None,fx=0.5, fy=0.5, interpolation = cv.INTER_CUBIC) #right here we are using the same fuction as the last prorgam
cv.imwrite("canny.jpg", cv.Canny(res, 200, 300)) # Canny -> detects edges of the image 
cv.imshow("canny", cv.imread("canny.jpg")) #right here we display the changes we made to the object 
cv.waitKey()
cv.destroyAllWindows() # destroy the apps
 #this program reads a image object and cannies the object var