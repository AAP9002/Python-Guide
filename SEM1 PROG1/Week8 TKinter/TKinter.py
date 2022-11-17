from tkinter import Tk, PhotoImage,Label, Radiobutton,Button,IntVar
from random import randint, shuffle
def configureWindow():
    window.title("Maths Game")
    window.geometry("600x600")
    window.configure(background="#b3ffff")

window=Tk()

configureWindow()

# global variables
user_answer= IntVar() #used to pass variables between tk inter and python
btn = None
current_score = 0
score = Label(window,text="Score = 0", font=("Arial Bold",50),background='#b3ffff')
score.grid(column=2,row=8,columnspan=4,sticky="E")
correct = PhotoImage(file="./correct.png")
incorrect = PhotoImage(file="./incorrect.png")

def game_Loop():
    num1 = randint(1,20)
    num2 = randint(1,20)
    operator = randint(0,2) # + - *
    display_question(num1, num2, operator)
    answer = calculate_answer(num1,num2,operator)
    print(answer)
    answers = add_incorrect_answers(answer)
    create_answer_radio_buttons(answers)
    create_check_answer_button(answer)

def display_question(num1, num2, operator):
    operators = ["+","x","-"]
    question = str(num1)+" "+ operators[operator] + " " + str(num2)+"="
    question = Label(window, text=question, font=("Arial Bold",50),background='#b3ffff')
    question.grid(column = 1, row = 1, columnspan = 6, sticky="W")

def calculate_answer(num1, num2, operator):
    if operator == 0:
        return num1 + num2
    elif operator == 1:
        return num1 * num2
    elif operator == 2:
        return num1 - num2

def add_incorrect_answers(answer):
    answers = []
    answers.append(answer)
    for i in range(4):
        while True:
            number = randint(answer-10, answer+10)
            if (number not in answers):
                answers.append(number)
                break
    return answers

def create_answer_radio_buttons(answers):
    ans = []
    for i in range(len(answers)):
        ans.append(Radiobutton(window, text=answers[i], value=answers[i], font=("Arial Bold",50), indicatoron = 0, variable=user_answer, background="#b3ffff",selectcolor = "#99ff99",width=4))
        #indicatoron chenges the style of the radio button
    shuffle(ans)
    padding = Label(window, text=" ", font=("Arial Bold",25), background="#b3ffff")
    padding.grid(column = 1, row = 3)
    for i in range(len(ans)):
        ans[i].grid(column=i+2,row=3)
    padding.grid(column = 1, row = 4)

def create_check_answer_button(answer):
    global btn
    btn = Button(window, text="check answer", command=lambda:clicked(answer), background="#ffff4d", font=("Arial Bold",50))
    btn.grid(column=0,row=5,columnspan=7)

def clicked(answer):
    global current_score
    if (answer == user_answer.get()):
        btn.configure(text="Correct")
        current_score += 10
        ans_label = Label(window, image=correct)
        score.configure(text = "Score:" + str(current_score))
    else:
        btn.configure(text="Incorrect")
        ans_label = Label(window, image=incorrect)
    ans_label.grid(column=1,row=8,columnspan=2)
    window.after(1000,game_Loop)

game_Loop()

window.mainloop()