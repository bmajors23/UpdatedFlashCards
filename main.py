import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}


def known_word():
    global current_card
    with open("words_known.csv", "a") as words_known:
        words_known.write(f"{current_card['French']},{current_card['English']}\n")
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title_text, fill="black", text="French")
    current_card = random.choice(french_words_dict)
    new_french_word = (current_card["French"])
    canvas.itemconfig(word_text, fill="black", text=new_french_word)
    window.after(3000, func=flip_card)


def unknown_word():
    global current_card
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title_text, fill="black", text="French")
    current_card = random.choice(french_words_dict)
    new_french_word = (current_card["French"])
    canvas.itemconfig(word_text, fill="black", text=new_french_word)
    window.after(3000, func=flip_card)


def flip_card():
    global current_card
    new_english_word = (current_card["English"])
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=new_english_word, fill="white")


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
known_pic = PhotoImage(file="./images/right.png")
unknown_pic = PhotoImage(file="./images/wrong.png")

known_button = Button(image=known_pic, highlightthickness=0, command=known_word)
known_button.grid(column=1, row=1)

unknown_button = Button(image=unknown_pic, highlightthickness=0, command=unknown_word)
unknown_button.grid(column=0, row=1)

canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 262.5, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", font=("arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

try:
    unknown_words = pandas.read_csv("./words_to_learn.csv")
    french_words_dict = unknown_words.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    french_words = pandas.read_csv("./data/french_words.csv")
    french_words_dict = french_words.to_dict(orient="records")





window.mainloop()