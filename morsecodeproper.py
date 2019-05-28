import RPi.GPIO as GPIO
import time
from tkinter import *
import tkinter .font
from gpiozero import LED

## Hardware
red_led = LED(18)

## GUI Definitions
## New window called win and title for that window
win = Tk()
win.title("Morse Code")
entry = StringVar()
#set a font for items in the future, note weight sets the font as bold
myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")
#MorseString = ("Default").2)
def dot():
    GPIO.output(ledPin,1)
    time.sleep(0.2)
    GPIO.output(ledPin,0)
    time.sleep(0.2)

def dash():
    GPIO.output(ledPin,1)
    time.sleep(0.5)
    GPIO.output(ledPin,0)
    time.sleep(0.2)
    
def morseToggle():
    String = entry.get()
    while True:

        for letter in String:
            for symbol in CODE[letter.upper()]:
                if symbol == '-':
                    dash()
                elif symbol == '.':
                    dot()
                else:
                    time.sleep(0.5)
            time.sleep(0.5)

def exitToggle():
    quit()
    
def retrieve_input():
    MorseString = MorseEntry.get()
    
        
def exitToggle():
    quit()
        
##Widgets
#redButton = Button(win, text = "Turn red On", font = myFont, command = redToggle, bg = "bisque2", height = 1, width = 24)
#redButton.grid(row=0, column = 1)
MorseLabel = Label(win, text="Morse Statement").grid(row=0)
MorseEntry = Entry(win, font = myFont, textvariable = entry, width = 24)
MorseEntry.grid(row = 0, column = 1)
redButton = Button(win, text = "Translate", font = myFont, command = morseToggle, bg = "bisque2", height = 1, width = 24)
redButton.grid(row=1, column = 0)
exitButton = Button(win, text = "Exit Program", font = myFont, command = exitToggle, bg = "bisque2", height =1, width =24)
exitButton.grid(row = 1, column = 1) 
CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}
ledPin=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)


