import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#BC7AF9"

class QuizInterface:
    
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizz UP!")
        self.window.geometry("350x500") 
        self.window.config(pady=20, padx=25, bg=THEME_COLOR)
        self.window.resizable(False, False)
        
        self.score_label = tk.Label(text="Score: 0 ", fg="#FFECEC", bg=THEME_COLOR, font=('courier', 20, 'bold'))
        self.score_label.grid(row=0, column=1)
        
        self.canvas = tk.Canvas(width=300, height=250, bg= '#FDFFAE', border=0, highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=250,
                                                     text="Question goes here...",
                                                     fill='#40128B',
                                                     font=('Cooper Black', 17))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        
        true_image = tk.PhotoImage(file='D:/python/Quizapptk/images/true.png')
        self.true_btn = tk.Button(image=true_image, command=self.check_true, height=80, width=80, background="#1DDB82", highlightthickness=0)
        self.true_btn.grid(row=3, column=0, columnspan=1, padx=10)
        
        false_image = tk.PhotoImage(file='D:/python/Quizapptk/images/false.png')
        self.false_btn = tk.Button(image=false_image, command = self.check_false, height=80, width=80, background="#FF6969", highlightthickness=0)
        self.false_btn.grid(row=3, column=1, columnspan=1, padx=10)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(background="#FDFFAE")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= f"        QUIZZ UP\nYou've reached the end.\nYour final score is {self.quiz.score}/{self.quiz.question_number}", fill= "#1B3C73")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            
            
    def check_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
        

    def check_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="#74E291")
        else:
            self.canvas.config(background="#FF6868")
        self.window.after(1000, self.get_next_question)
        
        
        
    
