from guizero import App, PushButton
from gpiozero import LED

led17 = LED(17)

def GPIO_17():
    if button1.text == "GPIO17_ON ":
        button1.text = "GPIO17_OFF"
        led17.on()
    else:
        button1.text="GPIO17_ON "
        led17.off()
        
        
if __name__== "__main__":
    app = App("Activation GPIO")
    
    button1 = PushButton(app, command= GPIO_17, text= "GPIO17_ON")
    app.display()
    led17.off