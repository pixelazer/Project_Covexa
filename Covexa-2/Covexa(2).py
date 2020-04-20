'''
Covexa 2.0
[beta]
'''

import pyttsx3
import webbrowser
import pygame as pg
from time import sleep

engine = pyttsx3.init()

width = 800
height = 550
size = (width, height)

running = True

# Registering chrome
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

dialogues = {"a": "It is a new virus, tramsmitted to humans by bats.",
             "b": "Quarantine yourself if having symptoms or if you are in a city with any reported cases.",
             "c": 'Covid-19 transmits through mucous droplets that are sprayed into the air while sneezing or coughing.',
             'd': "Coronavirus originated in Wuhan, Hubei Province, China.",
             'e': "Symptoms of Coronavirus include cough, fever, chills, headache, tiredness, and trouble breathing.",
             'f': "Use alcohol-based hand sanitizer and rub thoroughly after coming in contact with any object which could be contaminated.",
             'g': "For regular updates on Covid-19 from the World Health Organization, Send 'hi' to + 4 1, 7 9 8, 9 3 1, 8 9 2 on WhatsApp.",
             'h': "Symptoms include coughing, sneezing, difficulty breathing, and pneumonia.",
             'z': "Hope you are well. Goodbye"}

screens = {1: 'bg1'}

# Initialises Speech Output
def speech_init(): 
    engine.setProperty('rate', 150)
    engine.setProperty('volume' , 2)
    voices = engine.getPropertyvoices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[0].id)
    
def speech_output(x):
    engine.say(x)
    engine.runAndWait()

def open_website(a):
    c = webbrowser.get('Chrome')
    c.open_new_tab(a)
    
def change_screen(image):
    bg = pg.image.load("images/"+ image +".png").convert_alpha()
    screen.blit(bg,(0,0))
    sleep(1)
    
    

""" Main Code """
    
speech_init()
pg.init()

screen = pg.display.set_mode(size)
change_screen('bg1')
pg.display.set_caption('Covexa')

# Startup
x = "I am covexa, your coronavirus help bot"
speech_output(x)
x = "Ask me any questions you have related to Coronavirus."
speech_output(x)
x = "To exit enter Z"
speech_output(x)
userinp = input().lower()

# Function that will run Covexa until user exits
while running:
    if "corona" in userinp:
        x = dialogues['a']
        speech_output(x)
        userinp = input().lower()
        
    if "precaution" in userinp:
        x = dialogues['b']
        speech_output(x)
        a = "https://www.who.int"
        open_website(a)
        userinp = input().lower()
        
    if "symptoms" in userinp:
        x = dialogues['h']
    
    if "transmission" in userinp:
        x = dialogues['c']
        speech_output(x)
        userinp = input().lower()
    
    if "origin" in userinp:
        x = dialogues['d']
        speech_output(x)
        userinp = input().lower()
        
    if "symptoms" in userinp:
        x = dialogues['e']
        speech_output(x)
        userinp = input().lower()
        
    if "updates" in userinp:
        x = dialogues['g']
        speech_output(x)
        b = "https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"
        open_website(b)
        userinp = input().lower()
    
    if "sanitizer" in userinp:
        x = dialogues['f']
        speech_output(x) 
        userinp = input().lower()
        
    if "z" in userinp:
        running = False
    else:
        change_screen('bg2')
        x = "I don't know the answer to that question"
        speech_output(x)
        change_screen('bg1')
        userinp = input().lower()

# Covexa will say this after exiting the while loop
x = dialogues['z']
speech_output(x)
x = "Have a good day!"
speech_output(x)

