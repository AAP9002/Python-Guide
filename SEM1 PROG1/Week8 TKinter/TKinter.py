from tkinter import Tk, PhotoImage,Label

def configureWindow():
    window.title("Maths Game")
    window.geometry("600x600")
    window.configure(background="#b3ffff")

def globalstuff():
    btn = None
    current_score = 0
    score = Label(window,text="Score = 0", font=("Arial Bold",50),background='#b3ffff')
    score.grid(column=2,row=8,columnspan=4,sticky="E")

    correct = PhotoImage(file="./correct.png")
    incorrect = PhotoImage(file="./incorrect.png")

window=Tk()

configureWindow()

globalstuff()

window.mainloop()