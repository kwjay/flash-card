from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")
word = {}


def new_word():
    global word, timer
    window.after_cancel(timer)
    word = random.choice(words)
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=word["French"], fill="black")
    canvas.itemconfig(card_img, image=card_front_file)
    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=word["English"], fill="white")
    canvas.itemconfig(card_img, image=card_back_file)


window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash Cards")

timer = window.after(3000, func=flip_card)

canvas = Canvas(bg=BACKGROUND_COLOR, height=600, width=900, highlightthickness=0)

card_front_file = PhotoImage(file="images/card_front.png")
card_back_file = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(450, 300, image=card_front_file)
language_label = canvas.create_text(450, 170, text="", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(450, 300, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(highlightthickness=0, image=right_img, command=new_word)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(highlightthickness=0, image=wrong_img, command=new_word)
wrong_button.grid(column=0, row=1)

new_word()

window.mainloop()
