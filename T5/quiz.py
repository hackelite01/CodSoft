import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import random

# questions
questions = [
    {
        'question': 'Which of these language uses "$" to declear a variable?',
        'choices': ['Python','Java','Golang','PHP'],
        'correct_answer': 'PHP'
    },
    {
        'question': 'Functions in a class are often refer to as?',
        'choices': ['Function','Methods','Class','Function','NONE'],
        'correct_answer': 'Methods'
    },
    {
        'question': 'What is the output of this expression, 3*1**3?',
        'choices': ['27', '9', '3', '1'],
        'correct_answer': '3'
    },
    {
        'question': 'Which of these is not a core data type in python?',
        'choices': ['Lists','Dictionary','Tuples','Class'],
        'correct_answer': 'Class'
    },
    {
        'question': 'What is the type of inf in python?',
        'choices': ['Boolean','Integer','Float','Complex'],
        'correct_answer': 'Float'
    },
    {
        'question': 'What is the Dev of this app?',
        'choices': ['Sunadar Pichai', 'Mark', 'Elon', 'Mayank'],
        'correct_answer': 'Mayank'
    }
]


class QuizGame:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.questions_copy = questions.copy()
        self.current_question = None
        self.selected_button = None

        self.question_label = tk.Label(root, text='', wraplength=400,
                                       font=Font(family='Poppins', size=14, weight='bold'))
        self.question_label.pack(pady=20)

        self.choices_buttons = []
        for _ in range(4):
            button = tk.Button(root, text='', width=30, font=Font(family='Poppins', size=12))
            button.pack(pady=5)
            self.choices_buttons.append(button)

        self.answer_label = tk.Label(root, text='', wraplength=400, font=Font(family='Poppins', size=12, weight='bold'))
        self.answer_label.pack(pady=20)

        self.next_question()

    def next_question(self):
        if len(self.questions_copy) > 0:
            self.current_question = random.choice(self.questions_copy)
            self.question_label.config(text=self.current_question['question'])

            choices = self.current_question['choices']
            random.shuffle(choices)

            for i, button in enumerate(self.choices_buttons):
                button.config(text=choices[i])
                button.config(command=lambda b=button: self.button_selected(b))
                button.config(state='normal')

            self.selected_button = None
            self.answer_label.config(text='')
        else:
            self.show_results()

    def button_selected(self, button):
        self.selected_button = button
        self.check_answer()

    def check_answer(self):
        if self.selected_button is not None:
            user_answer = self.selected_button['text']
            correct_answer = self.current_question['correct_answer']

            if user_answer == correct_answer:
                self.score += 1
                self.answer_label.config(text='Your answer is correct!', fg='green')
            else:
                self.answer_label.config(text=f'Your answer is incorrect!\nThe correct answer is: {correct_answer}',
                                         fg='red')

            self.selected_button.config(state='disabled')
            self.questions_copy.remove(self.current_question)
            self.root.after(1000, self.next_question)

    def show_results(self):
        result_text = f'Final Score: {self.score}/{len(questions)}'
        self.answer_label.config(text=result_text, fg='black')

        play_again = messagebox.askyesno('Play Again', 'Do you want to play again?')
        if play_again:
            self.score = 0
            self.questions_copy = questions.copy()
            random.shuffle(self.questions_copy)
            self.next_question()
        else:
            self.root.destroy()


# Creating the main window
root = tk.Tk()
root.title('Quiz Game')
root.geometry('500x500')

# Creating an instance of the QuizGame class
game = QuizGame(root)

# Creating an Credit Label
Credit_label = tk.Label(root, text='Made By Mayank Rajput', wraplength=400,
                        font=Font(family='Poppins', size=12, weight='bold'), fg="Orange")
Credit_label.pack()

# Start the GUI
root.mainloop()
