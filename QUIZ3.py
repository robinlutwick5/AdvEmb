# -*- coding: utf-8 -*-
"""
Created on Thu Feb 4 18:43:30 2021

@author: Robin Lutwick
"""

from gpiozero import LED, Button
from guizero import App, Text, TextBox, PushButton
from threading import Thread
from time import sleep

RL = LED(16)
YL = LED(20)
GL = LED(26)
CL = LED(21)
button = Button(19, pull_up=True) #We're using our trusty pull up resistor in

def crossx(): 
    while True:
        Text1.value = RL.value
        Text2.value = YL.value
        Text3.value = GL.value
        Text4.value = CL.value

def READ_MY_BUTTON_THREAD():
    while True:
        
        if button.is_pressed:
            print("the cross walk button pressed")
            GL.off()
            Text1.value = "Green light turned Off"
            sleep(.4)
            YL.on()
            Text2.value = "Yellow light turned On"
            sleep(3)
            YL.off()
            Text2.value = "Yellow light turned Off"
            RL.on()
            Text3.value = "Red light turned On"
            CL.on()
            Text4.value = "Cross Safely"
            sleep(5)
            RL.off()
            Text3.value = "Red light turned Off"
            CL.off()
            Text4.value = "Don't Walk"

        else:
            GL.on()
            
            Text1.value = "Green light turned On"
            Text2.value = "Yellow Light turned Off"
            Text3.value = "Red Light turned Off"
            Text4.value = "Don't Cross"
            
            sleep(1)

if __name__ == '__main__':

    app = App("Traffic Lights on the Pi ", height=500, width=500, layout="grid")

    Text1 = TextBox(app, width=100, grid=[1, 0], command=crossx)
    Text2 = TextBox(app, width=100, grid=[1, 1], command=crossx)
    Text3 = TextBox(app, width=100, grid=[1, 2], command=crossx)
    Text4 = TextBox(app, width=100, grid=[1, 3], command=crossx)
    
    thread = Thread(target=READ_MY_BUTTON_THREAD)
    thread.start()
    app.display()
