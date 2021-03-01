"""
Created on Sun Feb 22 09:55:57 2021

@author: Robin Lutwick
"""

import serial
import guizero 
import time

ser = serial.Serial('/dev/ttyACM0', 9600) #this must be set to our baudrate on our arduino along with the device port taken from inclass notes
ser.flush()#this clears the buffer                        
time.sleep(3)                      

Ser1_Pos = []  #this is our container for Servo 1's Postion                    
Ser2_Pos = []                    

def Write_Pos(): #this is our function for writing the postion of our servos to memory when asked to save by the user

    Ser1_Pos.append(slider1.value)
    Ser2_Pos.append(slider2.value)

def Last_Pos():

    for i in range(0,len(Ser1_Pos)):#This iterates an array to encode the data up to length of the message, send the data to go to last postions with accuracy 

        ser.write(str('M1').encode('utf-8'))
        ser.write(str("\n").encode('utf-8'))
        ser.flush()
        
        ser.write(str(Ser1_Pos[i]).encode('utf-8'))
        ser.write(str("\n").encode('utf-8'))
        ser.flush()

        ser.write(str('M2').encode('utf-8'))
        ser.write(str("\n").encode('utf-8'))
        ser.flush()
        
        ser.write(str(Ser2_Pos[i]).encode('utf-8'))
        ser.write(str("\n").encode('utf-8'))
        ser.flush()

def slider1_read(slider_value):#this function reads the value of our sliders encodes it and then commits the data to memory

    a = slider_value
    ser.flush()
    print(slider_value)
    
    ser.write(str('M1').encode('utf-8'))
    ser.write(str("\n").encode('utf-8'))
    ser.flush()
    
    ser.write(str(slider_value).encode('utf-8'))
    ser.write(str("\n").encode('utf-8'))
    time.sleep(.3)
    return a

def slider2_read(slider_value):

    print(slider_value)
    ser.flush()
    ser.write(str('M2').encode('utf-8'))
    ser.write(str("\n").encode('utf-8'))
    ser.flush()
    ser.write(str(slider_value).encode('utf-8'))
    ser.write(str("\n").encode('utf-8'))
    time.sleep(.2)



app = guizero.App("Slider Servo Motor Control", height=400, width=400)

slider1 = guizero.Slider(app, start=0, end=180, width="fill", command=slider1_read)
slider2 = guizero.Slider(app, start=0, end=180, width="fill", command=slider2_read)

RecordButton = guizero.PushButton(app, text="Save This Position", command=Write_Pos)
RepeatButton = guizero.PushButton(app, text="Go To Last Position", command=Last_Pos)

app.display()

ser.close()



#you gave us this at the start for reference
# import Serial
# from time import sleep
# 
# ser = serial.Serial('COM', 9600)
# 
# ser.flush()
# dato=0.90
# ser.write(str(dato(0)).encode('utf-8'))
# print(dato)
# sleep(1)
# ser.close()