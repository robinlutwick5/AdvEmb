from gpiozero import PWMLED
from time import sleep
import math as m

led = PWMLED(17)

itr = 0
inc = 0
bri = 0
brilvl = 10
theta = 0
ton = 3.3

while itr < 10:
    while inc <= brilvl:
        
        theta = (inc/brilvl)*(m.pi)
        bri = m.sin(theta)
        led.value = bri
        ot = ton/brilvl
        sleep(ot)
        inc+=1
        
    itr+=1
    inc=0        