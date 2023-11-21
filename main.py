from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash Cards")

canvas = Canvas(bg=BACKGROUND_COLOR, height=600, width=900, highlightthickness=0)

card_file = PhotoImage(file="images/card_front.png")
card_img = canvas.create_image(450, 300, image=card_file)
language_label = canvas.create_text(450, 170, text="French", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(450, 300, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


right_img = PhotoImage(file="images/right.png")
right_button = Button(highlightthickness=0, image=right_img)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(highlightthickness=0, image=wrong_img)
wrong_button.grid(column=0, row=1)

window.mainloop()
