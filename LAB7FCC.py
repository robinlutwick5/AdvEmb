from guizero import App, Text
from gpiozero import Button
from gpiozero import LED

button = Button(2)
led = LED(17)

def scanInput():
    if button.is_pressed:
        text.value = 1
        led.on()
    else:
        text.value = 0
        led.off()
        
def exitGUI():
    
    text.destroy()
    if app.yesno("Close", "Do you want to Quit:(?"):
        app.destroy()
        print("Adios")
        
if __name__ == '__main__':
    
    app = App("Reading GPIO")
    text = Text(app, text="1")
    text.repeat(10, scanInput)
    input(every)
    app.when_closed = exitGUI
    app.display()