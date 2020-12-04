from turtle import reset, left, forward, right
from tkinter import Tk, Button

settings = {
    "LineLengthOne": 50,
}

def buttonIncreaseOneFunction():
    settings["LineLengthOne"] = int(settings["LineLengthOne"]) + 10
    print("buttonIncreaseOneFunction new line length: " + str(settings["LineLengthOne"]))
    
def buttonDecreaseTwoFunction():
    settings["LineLengthOne"] = int (settings["LineLengthOne"]) - 10
    print("buttonDecreaseTwoFunction new line length: " + str(settings["LineLengthOne"]))

def buttonDraw():
    print("buttonDraw pressed")
    reset()
    forward(settings["LineLengthOne"])
    



window = Tk()

print("Loading...")
buttonIncreaseOne = Button(window, text="Click to increase.", command=buttonIncreaseOneFunction)
buttonDecreaseTwo = Button(window, text="Click to decrease.", command=buttonDecreaseTwoFunction)
buttonTurtle = Button(window, text="Draw.", command=buttonDraw)
buttonIncreaseOne.pack()
buttonDecreaseTwo.pack()
buttonTurtle.pack()
# true = False
#while not true:
#    print("Your current value is "+ str(settings["LineLengthOne"]) +".")
