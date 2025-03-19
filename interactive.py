# interactive game
# authors: lucia Alday and Emily Bauman
# last modified: 3/17/2025

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# what if we do one list of severities so the amount is the same for each animal
# and then we each animal with its own list of prompts

# EVENTS = {"basic prompt": "severity (integer)"}
SNAKE_EVENTS = {}
OWL_EVENTS = {}
COYOTE_EVENTS = {}
SCORPION_EVENTS = {}
JAVELINA_EVENTS = {}

EASY_MAX = 600
MED_MAX = 450
HARD_MAX = 300
MAX_ROUNDS = 3      # number of rounds


class Player:
    def __init__(self, name='', animal_name='', difficulty='Easy'):
        '''
        name: string for player name
        animal_name: name of animal player chose
        difficulty: string for easy, medium, or hard difficulty
        '''
        self.name = name
        self.difficulty = difficulty
        self.animal_name = animal_name
        self.points = 0
    
    def set_vals(self):
        if self.animal_name == "Rattlesnake":
            imagepath = './snake.jpg'
            self.animal = Animal("Rattlenake", imagepath)
            self.events = self.animal.build_snake_events() # events are TBD
        elif self.animal_name == "Owl":
            imagepath = './owl.jpg'
            self.animal = Animal("Owl", imagepath)
            self.events = self.animal.build_owl_events()
        elif self.animal_name == "Coyote":
            imagepath = './coyote.jpg'
            self.animal = Animal("Coyote", imagepath)
            self.events = self.animal.build_coyote_events()
        elif self.animal_name == "Scorpion":
            imagepath = './scorpion.jpg'
            self.animal = Animal("Scorpion", imagepath)
            self.events = self.animal.build_scorpion_events()
        elif self.animal_name == "Javelina":
            imagepath = './javalina.jpg'
            self.animal = Animal("Javelina", imagepath)
            self.events = self.animal.build_javelina_events()
        
        if self.difficulty == "Easy":
            self.max_health = EASY_MAX
            self.health = EASY_MAX
        elif self.difficulty == "Medium":
            self.max_health = MED_MAX
            self.health = MED_MAX
        else:
            self.max_health = HARD_MAX
            self.health = HARD_MAX
        
        self.lives = 3

    def event_outcome(self, outcome, severity):
        '''
        - outcome is a boolean, True is good, bad is False
        - insert good/ bad outcomes
        - good means health go up, bad means health goes down
        - if health equals 0, they lose a life and health resets
        '''
        if outcome:
            self.points += severity
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

PLAYER = Player()

class Animal:
    def __init__(self, animal='', filename=''):
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
    def __init__(self, event_name='', severity=0):
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
        phrase += "Severity: " + str(self.severity)
        return phrase

def create_window():
    root = Tk()
    root.title('Game')
    root.geometry('600x450')

    #img = Image.open('./desert-museum-photo.jpg').convert('RGBA')
    img = Image.open('./pricklypear.jpg').convert('RGBA')
    img = img.resize((800, 1200));
    img = ImageTk.PhotoImage(image=img, master=root)

    img_label = Label(root, image=img)
    img_label.place(x=0, y=0, relheight=1, relwidth=1)

    # player name
    name_label = Label(root, text="Player Name: ")
    name_label.grid(row=0, column=0, sticky='ne', padx=20, pady=50)

    name_entry = Entry(root)
    name_entry.grid(row=0, column=1, sticky='ew')

    # animal
    animal_select = Label(root, text='Choose your animal!')
    animal_select.grid(row=1, column=0, padx=20, pady=20)

    animal_entry = StringVar()
    animal_entry.set('Owl')
    # owl
    owl_entry = Radiobutton(root, text='Owl', variable=animal_entry, value='Owl')
    owl_entry.grid(row=2, column=0, sticky='w', padx=20)
    # rattlesnake
    snake_entry = Radiobutton(root, text='Rattlesnake', variable=animal_entry, value='Rattlesnake')
    snake_entry.grid(row=3, column=0, sticky='w', padx=20)
    # javelina
    javelina_entry = Radiobutton(root, text='Javelina', variable=animal_entry, value='Javelina')
    javelina_entry.grid(row=4, column=0, sticky='w', padx=20)
    # coyote
    coyote_entry = Radiobutton(root, text='Coyote', variable=animal_entry, value='Coyote')
    coyote_entry.grid(row=5, column=0, sticky='w', padx=20)
    # scorpion
    scorpion_entry = Radiobutton(root, text='Scorpion', variable=animal_entry, value='Scorpion')
    scorpion_entry.grid(row=6, column=0, sticky='w', padx=20)

    # difficulty
    difficulty_select = Label(root, text='Choose your difficulty!')
    difficulty_select.grid(row=1, column=3)

    difficulty_entry = StringVar()
    difficulty_entry.set('easy')
    # easy
    easy_entry = Radiobutton(root, text='Easy', value='easy', variable=difficulty_entry)
    easy_entry = Radiobutton(root, text='Easy', value='easy', variable=difficulty_entry)
    easy_entry.grid(row=2, column=3, sticky='w')
    # medium
    med_entry = Radiobutton(root, text='Medium', value='medium', variable=difficulty_entry)
    med_entry.grid(row=3, column=3, sticky='w')
    # hard
    hard_entry = Radiobutton(root, text='Hard', value='hard', variable=difficulty_entry)
    hard_entry.grid(row=4, column=3, sticky='w')

    # collect input info
    def collect_info():
        if name_entry.get()=='':
            PLAYER.name = 'Kid'
        else:
            PLAYER.name = name_entry.get()
        PLAYER.animal_name = animal_entry.get()
        PLAYER.difficulty = difficulty_entry.get()

    # start
    start_button = Button(root, text='Start Game!', command=lambda:[collect_info(), PLAYER.set_vals(), root.destroy(), show_stats(0)])
    start_button.grid(row=7, column=1, pady=50, padx=100)

    root.mainloop()

def show_stats(n):
    root2 = Tk()
    root2.title('Player Stats')
    root2.geometry('300x300')

    # show animal background image
    img2 = Image.open(PLAYER.animal.filename).convert('RGBA')
    img2.thumbnail((500, 500))
    img2 = ImageTk.PhotoImage(image=img2, master=root2)
    img_label = Label(root2, image=img2)
    img_label.place(x=0, y=0, relheight=1, relwidth=1)


    # show selection
    animal_label = Label(root2, text=(PLAYER.animal_name+' '+PLAYER.name))
    animal_label.grid(column=0, row=1, padx=200, pady=20, sticky='ew')

    health_label = Label(root2, text=(str(PLAYER.lives)+' lives remaining'))
    health_label.grid(column=0, row=2, padx=200, pady=20, sticky='ew')

    points_label = Label(root2, text=(str(PLAYER.points)+' points accrued'))
    points_label.grid(column=0, row=3, padx=200, pady=20, sticky='ew')

    continue_button = Button(root2, text='Continue', command=lambda:[root2.destroy(), start_round(n+1)])
    continue_button.grid(column=0, row=6, padx=200, pady=60)

    root2.mainloop()

def start_round(n):
    if n == MAX_ROUNDS:
        win_sequence()
        return
    if PLAYER.is_dead():
        lose_sequence()
        return
    root1 = Tk()
    root1.title('Round '+ str(n))
    root1.geometry('700x600')

    root1.mainloop()

def outcome(n):
    start_round(n+1)        # advance to next round
    return

def win_sequence():
    root4 = Tk()
    root4.title('You win!')
    root4.geometry('300x300')
    # show animal background image
    img2 = Image.open('./sunset.jpg').convert('RGBA')
    img2.thumbnail((550, 550))
    img2 = ImageTk.PhotoImage(image=img2, master=root4)
    img_label = Label(root4, image=img2)
    img_label.place(x=0, y=0, relheight=1, relwidth=1)

    win = Label(root4, text='Congratulations '+PLAYER.animal_name+' '+PLAYER.name+'!\nYou survived the monsoon storm with '+str(PLAYER.points)+' points!')
    win.place(relx=0.5, rely=0.5, anchor='center')

    play_again = Button(root4, text='Play Again', command=lambda:[root4.destroy(), create_window()])
    play_again.place(relx=0.5, rely=0.7, anchor='center')
    
    root4.mainloop()

def lose_sequence():
    root5 = Tk()
    root5.title('You lost :(')
    root5.geometry('300x300')

    # show animal background image
    img2 = Image.open('./lightning.png').convert('RGBA')
    img2.thumbnail((550, 550))
    img2 = ImageTk.PhotoImage(image=img2, master=root5)
    img_label = Label(root5, image=img2)
    img_label.place(x=0, y=0, relheight=1, relwidth=1)

    loss = Label(root5, text='Oh no '+PLAYER.animal_name+' '+PLAYER.name+'!\nThe monsoon was too strong!\nYou lost with '+str(PLAYER.points)+' points.')
    loss.place(relx=0.5, rely=0.5, anchor='center')

    play_again = Button(root5, text='Play Again', command=lambda:[root5.destroy(), create_window()])
    play_again.place(relx=0.5, rely=0.7, anchor='center')
    
    root5.mainloop()

win_sequence()
#create_window()



