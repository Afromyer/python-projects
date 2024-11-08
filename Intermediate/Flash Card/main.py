from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WON_COLOR = "#FDD813"

TIMER_AMOUNT = 3000

data = pandas.read_csv("./data/Afrikaans-English.csv")

french_words = data.to_dict(orient="dict")

try:
    data_to_learn = pandas.read_csv("./data/words_to_learn.csv")
    words_to_learn = data_to_learn.to_dict(orient="dict")
except FileNotFoundError:
    words_to_learn = french_words
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)

if len(words_to_learn[list(words_to_learn.keys())[0]]) == 0:
    words_to_learn = french_words
    new_data = pandas.DataFrame(words_to_learn)
    new_data.to_csv("./data/words_to_learn.csv", index=False)

current_index = random.choice(list(words_to_learn[list(words_to_learn.keys())[0]].keys()))
current_language = list(words_to_learn.keys())[0]


def right():
    global current_index
    global current_language
    global timer

    if current_language == list(words_to_learn.keys())[1]:
        try:
            del words_to_learn[list(words_to_learn.keys())[0]][current_index]
            del words_to_learn[list(words_to_learn.keys())[1]][current_index]
            save_data = pandas.DataFrame(words_to_learn)
            save_data.to_csv("./data/words_to_learn.csv", index=False)
            current_index = random.choice(list(words_to_learn[list(words_to_learn.keys())[0]].keys()))
        except KeyError:
            # Only gives a KeyError() when it can't find an index (Which means all words are guessed correctly)
            win()
        except IndexError:
            win()
        else:
            current_language = list(words_to_learn.keys())[0]
            show_card(current_language, current_index)
            window.after_cancel(timer)
            timer = window.after(TIMER_AMOUNT, show_answer)


def wrong():
    global current_index, current_language, timer

    if current_language == list(words_to_learn.keys())[1]:
        current_index = random.choice(list(words_to_learn[list(words_to_learn.keys())[0]].keys()))
        current_language = list(words_to_learn.keys())[0]
        show_card(current_language, current_index)
        window.after_cancel(timer)
        timer = window.after(TIMER_AMOUNT, show_answer)


def show_card(language, index):
    global current_language
    card.itemconfig(language_text, text=language.title())

    if language == list(words_to_learn.keys())[1]:
        current_language = list(words_to_learn.keys())[1]
        word = french_words[list(words_to_learn.keys())[1]][index]
        card.itemconfig(card_image, image=card_back)
        card.itemconfig(word_text, text=word, fill="white")
        card.itemconfig(language_text, fill="white")
    elif language == list(words_to_learn.keys())[0]:
        current_language = list(words_to_learn.keys())[0]
        word = french_words[list(words_to_learn.keys())[0]][index]
        card.itemconfig(card_image, image=card_front)
        card.itemconfig(word_text, text=word, fill="black")
        card.itemconfig(language_text, fill="black")


def show_answer():
    show_card(list(words_to_learn.keys())[1], current_index)


def win():
    window.after_cancel(timer)
    card.itemconfig(language_text, text="Congratulations!")
    card.itemconfig(word_text, text="All words correct")


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(TIMER_AMOUNT, show_answer)

card_front = PhotoImage(file="./Images/card_front.png")
card_back = PhotoImage(file="./Images/card_back.png")
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card.create_image(400, 263, image=card_front)
card.grid(row=0, column=0, columnspan=2)

language_text = card.create_text(400, 150, text=list(words_to_learn.keys())[0], font=("Ariel", 40, "italic"),
                                 fill="black")

word_text = card.create_text(400, 263, text=french_words[current_language][current_index], font=("Ariel", 60, "bold"),
                             fill="black")

# Buttons
wrong_image = PhotoImage(file="./Images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong, border=False)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./Images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right, border=False)
right_button.grid(row=1, column=1)

window.mainloop()
