from tkinter import *
import pandas as pd


# ---------------------------- CONSTANTS ------------------------ #

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- SELECT WORDS --------------------- #

word_list = pd.read_csv("data/french_words.csv")


# ---------------------------- BUTTONS COMAND --------------------- #


# ---------------------------- UI ------------------------------- #

window = Tk()
window.title("Flash Card Game")
window.config(pady=50, bg=BACKGROUND_COLOR)

# Getting image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=1, row=1, padx=50, columnspan=2)

# Texts

french = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
canvas.itemconfig(french, text="French")
word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.itemconfig(word, text="word")


# Buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(column=1, row=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=2, row=2)




window.mainloop()