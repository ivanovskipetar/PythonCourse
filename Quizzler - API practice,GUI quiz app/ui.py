from tkinter import *

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0

        self.score_label = Label(text=f"Score:{self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.q_text = self.canvas.create_text(150, 125, text="00:00", fill="black", font=(FONT_NAME, 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        wrong_img = PhotoImage(file="./images/false.png")
        self.button_wrong = Button(image=wrong_img, highlightthickness=0)
        self.button_wrong.grid(row=2, column=1)
        right_img = PhotoImage(file="./images/true.png")
        self.button_right = Button(image=right_img, highlightthickness=0)
        self.button_right.grid(row=2, column=0)

        self.window.mainloop()
