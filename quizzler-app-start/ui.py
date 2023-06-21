from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizUi:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text='Some Questions Text',
                                                     fill=THEME_COLOR,
                                                     font=("Arial",28,'italic'),
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        T_image = PhotoImage(file="images/true.png")
        self.Tbutton = Button(image=T_image, command=self.true_pressed)
        self.Tbutton.grid(row=2, column=0)
        F_image = PhotoImage(file = "images/false.png")
        self.Fbutton = Button(image=F_image, command=self.false_pressed)
        self.Fbutton.grid(row = 2, column=1)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text = question_text)

    def true_pressed(self):
        self.quiz.check_answer("True")
        score = self.quiz.score
        q_num = self.quiz.question_number
        self.score_label.config(text=f"Score {score}/{q_num}")
        self.next_question()

    def false_pressed(self):
        self.quiz.check_answer("False")
        score = self.quiz.score
        q_num = self.quiz.question_number
        self.score_label.config(text=f"Score {score}/{q_num}")
        self.next_question()