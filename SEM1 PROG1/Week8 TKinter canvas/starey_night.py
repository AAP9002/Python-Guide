from tkinter import Tk, Canvas
from random import randint as rand

window = Tk()

canvas = Canvas(window, width=400,height=400,bg="black")
canvas.pack()

stars = []
c=["white","#fefefe","#dfdfdf"]
for i in range(1000):
    x = rand(0,799)
    y = rand(0,200)
    size = rand(1,4)
    color = c[rand(0,len(c)-1)]
    xy = (x,y,x+size,y+size)
    tempstar = canvas.create_oval(xy,fill=color)
    stars.append(tempstar)


# canvas.config # edit canvas
# canvas.itemconfig # edit items


window.mainloop()