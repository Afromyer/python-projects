from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.game_over = False
        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 20, "normal"))
        self.score_label.grid(row=0, column=1, sticky="e")

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, width=100, height=97, highlightthickness=0, borderwidth=0,
                                  command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, width=100, height=97, highlightthickness=0, borderwidth=0,
                                   command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def timer(self):
        if not self.game_over:
            self.canvas.config(bg="white")
            if self.quiz.still_has_questions():
                self.get_next_question()
        else:
            self.canvas.config(bg="yellow")
            self.canvas.itemconfig(self.question_text, text=f"Final Score: {self.quiz.score}")

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        if not self.game_over:
            if self.quiz.check_answer("True"):
                self.canvas.config(bg="green")
            else:
                self.canvas.config(bg="red")
            self.window.after(1000, self.timer)
            self.score_label.config(text=f"Score: {self.quiz.score}")
            if self.quiz.question_number == len(self.quiz.question_list):
                self.game_over = True

    def false_pressed(self):
        if not self.game_over:
            if self.quiz.check_answer("False"):
                self.canvas.config(bg="green")
            else:
                self.canvas.config(bg="red")
            self.window.after(1000, self.timer)
            self.score_label.config(text=f"Score: {self.quiz.score}")
            if self.quiz.question_number == len(self.quiz.question_list):
                self.game_over = True
