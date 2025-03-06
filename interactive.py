#interactive game

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

SNAKE_EVENTS = {"basic prompt": "severity (integer)"}
OWL_EVENTS = {}
COYOTE_EVENTS = {}
SCORPION_EVENTS = {}
JAVELINA_EVENTS = {}

class Player:
    def __init__(self, name, animal_name, difficulty):
        '''
        name: string for player name
        animal_name: name of animal player chose
        difficulty: string for easy, medium, or hard difficulty
        '''
        self.name = name
        
        if animal_name == "snake":
            self.animal = Animal("snake")
            self.events = self.animal.build_snake_events() # events are TBD
        elif animal_name == "owl":
            imagepath = '' # filename for photo is TBD
            self.animal = Animal("owl", imagepath)
            self.events = self.animal.build_owl_events()
        elif animal_name == "coyote":
            imagepath = ''
            self.animal = Animal("coyote", imagepath)
            self.events = self.animal.build_coyote_events()
        elif animal_name == "scorpion":
            imagepath = ''
            self.animal = Animal("scorpion", imagepath)
            self.events = self.animal.build_scorpion_events()
        elif animal_name == "javelina":
            imagepath = ''
            self.animal = Animal("javelina", imagepath)
            self.events = self.animal.build_javelina_events()
        
        if difficulty.lower() == "easy":
            self.max_health = 500
            self.health = 500
        elif difficulty.lower() == "medium":
            self.max_health = 400
            self.health = 400
        else:
            self.max_health = 300
            self.health = 300
        
        self.lives = 3

    def event_outcome(self, outcome, severity):
        '''
        - outcome is a boolean, True is good, bad is False
        - insert good/ bad outcomes
        - good means health go up, bad means health goes down
        - if health equals 0, they lose a life and health resets
        '''
        if outcome:
            self.health += severity
        else:
            self.health -= severity
    
    def lose_life(self):
        '''
        Checks if the player loses a life, returns true if the player lost
        a life and false otherwise.
        '''
        if self.health <= 0:
            self.lives -= 1
            self.health = self.max_health
            return True
        return False
    
    def is_dead(self):
        '''
        Checks if player has died.
        '''
        if self.lives == 0:
            return True
        return False
    
    def begin_event(self):
        '''
        Will only be called in main if self.events is not empty
        '''
        return self.events.pop()
    
    def current_health(self):
        '''
        Returns current health of the player, will be displayed as health bar
        for health and hearts for lives.
        '''
        return self.lives, self.health

class Animal:
    def __init__(self, animal, filename):
        '''
        animal: string for animal name
        filename: the name of the file for the image of the animal
        '''
        self.animal = animal
        self.filename = filename
    
    def name(self):
        return self.animal
    
    def display_photo(self):
        '''
        Displays the photo for the animal.
        '''
        pass

    def build_snake_events(self):
        events = []
        for key, value in SNAKE_EVENTS.items():
            events.append(Event(key,value))
        return events

    def build_owl_events(self):
        events = []
        for key, value in OWL_EVENTS.items():
            events.append(Event(key,value))
        return events

    def build_coyote_events(self):
        events = []
        for key, value in COYOTE_EVENTS.items():
            events.append(Event(key,value))
        return events
    
    def build_scorpion_events(self):
        events = []
        for key, value in SCORPION_EVENTS.items():
            events.append(Event(key,value))
        return events
    
    def build_javelina_events(self):
        events = []
        for key, value in JAVELINA_EVENTS.items():
            events.append(Event(key,value))
        print("hello")
        return events


class Event:
    def __init__(self, event_name, severity):
        '''
        event_name: the string for the description of the event
        severity: how many health points the player will win or lose if the event is completed
        '''
        self.event_name = event_name
        self.severity = severity
        
        # determines the difficulty of each event
        if severity <= 10:
            self._difficulty = "easy"
        elif severity <= 20:
            self._difficulty = "medium"
        else:
            self._difficulty = "hard"
    
    def difficulty(self):
        # returns how hard the event is if the player wants to know
        return self._difficulty
    
    def event(self):
        return self.event_name
    
    def __str__(self):
        phrase = "Difficulty: "+ self._difficulty + "\n"
        phrase += self.event_name + "\n"
        phrase += "Severity: " + self.severity
        return phrase



# health bar shows proportions not the values, show number of lives at the bottom of the screen

def create_window():
    root = Tk()
    root.title('Game')
    root.geometry('700x600')

    img = Image.open('./desert-museum-photo.jpg').convert('RGBA')
    img = ImageTk.PhotoImage(image=img, master=root)

    img_label = Label(root, image=img)
    img_label.place(x=0, y=0, relheight=1, relwidth=1)

    start_button = Button(text='Start Game!', command=lambda:[root.destroy(), start_round()])
    start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    root.mainloop()


def start_round():
    root1 = Tk()
    root1.title('')

    root1.mainloop()


create_window()



