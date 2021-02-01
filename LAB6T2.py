from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init()

button_sounds = {
    Button(2): Sound("applause-2.wav"),
    Button(3): Sound("applause-1.wav"),
    
    }

for button, sound in button_sounds.items():
    button.when_pressed = sound.play
    
    
pause()