#interactive game

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class Player:
    def __init__(self, name, animal, difficulty):
        self.name = name
        self.animal = animal    # note that this is an animal object not a string
        if animal == "owl":
            self.events = ['']
        if difficulty == "easy":
            health = 500
        elif difficulty == "medium":
            health = 400
        else:
            health = 300
        

        self.points = 0
        self.lives = 3
    def event(self, outcome, severity):
        # outcome is a boolean - True is good, bad is false
        # insert good/bad outcomes
        # good means points go up
        # bad means health goes down
        # if health = 0, then lose a life and health resets
        return


# different animals have different goals
class Animal:
    def __init__(self, animal):
        self.animal = animal



# health bar shows proportions not the values, show number of lives at the bottom of the screen

def create_window():
    root = Tk()
    root.title('Game')
    root.geometry('700x600')

    img = Image.open('desert-museum-photo.jpg')
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



