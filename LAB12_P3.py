#this program takes two object images and blends them together using the cv2 module cv.addWeighted()
#we display the end result in the end as a 3rd different object

import numpy as np #import numpy as np for short
import cv2 as cv #import cv2 as cv for short
import sys #import sys

img1 = cv.imread('Gopher.jpg') #create an object called img1 and set it to the gopher scene image from the movie caddy shack
img2 = cv.imread('FNH.jpeg') #create an object called img2 and set it to the woods picture from the movie the Fox and the Hound

alpha = 0.5 # i changed the factor to 0.5 so we could see the transisition much much clear
# alpha = 0.2
dst = cv.addWeighted(img1,1-alpha,img2,alpha,0) #this is the function that does the magic, it gives the altered object back to a var called dst
cv.imshow('dst',dst) # we display the object with this function and give it the title dst
cv.waitKey(0)
cv.destroyAllWindows() #close everything and all apps