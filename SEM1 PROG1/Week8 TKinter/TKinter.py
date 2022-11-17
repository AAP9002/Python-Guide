from tkinter import Tk, PhotoImage,Label
from random import randint as rand
def configureWindow():
    window.title("Maths Game")
    window.geometry("600x600")
    window.configure(background="#b3ffff")

window=Tk()

configureWindow()

# global variables
btn = None
current_score = 0
score = Label(window,text="Score = 0", font=("Arial Bold",50),background='#b3ffff')
score.grid(column=2,row=8,columnspan=4,sticky="E")
correct = PhotoImage(file="./correct.png")
incorrect = PhotoImage(file="./incorrect.png")

def game_Loop():
    num1 = rand(1,20)
    num2 = rand(1,20)
    operator = rand(0,2) # + - *
    display_question(num1, num2, operator)
    answer = calculate_answer(num1,num2,operator)
    answers = add_incorrect_answers(answer)

def display_question(num1, num2, operator):
    operators = ["+","x","-"]
    question = str(num1)+" "+ operators[operator] + " " + str(num2)+" = "
    question = Label(window, text=question, font=("Arial Bold",50),background='#b3ffff')
    question.grid(column = 1, row = 1, columnspan = 6, sticky="W")

def calculate_answer(num1, num2, operator):
    match operator:
        case 0:
            return num1+num2
        case 1:
            return num1 * num2
        case 2:
            return num1 - num2

def add_incorrect_answers(answer):
    answers = []
    answers.append(answer)
    for i in range(4):
        while True:
            number = rand(answer-10, answer+10)
            if (number not in answers):
                answers.append(number)
                break
    return answers

game_Loop()

window.mainloop()