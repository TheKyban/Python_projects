from tkinter import *
from brain import Brain


BACKGROUND = "#375362"
FONT = ("Ariel", 20, "italic")


class Gui:
    def __init__(self, brain: Brain):
        self.quiz = brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, background=BACKGROUND)

        self.label = Label(text="Score:0", background=BACKGROUND, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.text = self.canvas.create_text(150, 125, width=280, text="Question will be here", font=FONT, fill="purple")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Right Button
        self.t_img = PhotoImage(file="images/true.png")
        self.t_button = Button(image=self.t_img, highlightthickness=0, command=self.true_pressed)
        self.t_button.grid(row=2, column=1)

        # Wrong Button
        self.f_img = PhotoImage(file="images/false.png")
        self.f_button = Button(image=self.f_img, highlightthickness=0, command=self.false_pressed)
        self.f_button.grid(row=2, column=0)

        self.question_display()

        self.window.mainloop()

    def question_display(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            self.label.config(text=f"Score:{self.quiz.score}")
            self.canvas.itemconfig(self.text, text=self.quiz.next_questions())
        else:
            self.canvas.itemconfig(self.text, text="Over")
            self.f_button.config(state="disabled")
            self.t_button.config(state="disabled")
    def true_pressed(self):
        self.check(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.check(self.quiz.check_answer("False"))

    def check(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.question_display)

