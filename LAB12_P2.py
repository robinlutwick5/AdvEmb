#this program should take a video and display the grayscaled version to the user, i had some issues with this program and im not sure what is wrong:(

import numpy as np #bring numpy in and call it np for aberivation
import cv2 as cv # import cv2 module as cv 

#this program gave me a number of issues when i put my information in for instance right now when i compile it cannot read ret correctly
#earlier it could not find my camera so i re configured.

cap = cv.VideoCapture('MARYD.mp4')# this should name create an object called cap and set the object to my video file
if not cap.isOpened():#if the object is unable to be found & openned then print the message to the console window letting the user know 
    print("Cannot open camera")
    exit()
while True: #while the object is located run the code below
 # Capture frame-by-frame
    ret, frame = cap.read() #read the image object and return the reterval var and the image(frame)
 # if frame is read correctly ret is True
    if not ret:
     print("Can't receive frame (stream end?). Exiting ...")
     break #exit the condiational statement
 # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)#this converts our colored image to gray scale (black & white)

 # Display the resulting frame

    cv.imshow('frame', gray)
    #cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'): #the user can terminate the program by entering q to quit
        break
# When everything done, release the capture
    cap.release() #we mustt do this to clear the buffer so we can excute agin just like in C 
    cv.destroyAllWindows() #destory the windows so it doesnt keep running in the background