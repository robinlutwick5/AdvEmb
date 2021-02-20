# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 18:54:24 2021

@author: Robin Lutwick
"""

from guizero import App, Slider,TextBox
from gpiozero import AngularServo
import time 

ServoPin = 17

minPulseWidth = (1/1000)
maxPulseWidth = (2/1000)

def slider_change(slider_value):
    textbox.value = slider_value
    print(slider_value)
    servo1 = AngularServo(ServoPin, min_pulse_width = minPulseWidth, max_pulse_width = maxPulseWidth, initial_angle = 0, min_angle = -90, max_angle = 90)
    servo1.angle = int(slider_value)    
    time.sleep(0.5)    

app = App()
slider1 = Slider(app, start=-90, end=90, width="fill",command = slider_change)
textbox = TextBox(app)

print(textbox.value)

app.display()#this sends makes the app work and displays the changed our code has made

print(servo1.angle)#this prints what the current angle our servo is at, will print to the console window
