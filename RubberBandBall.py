import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides = int(input("Вы можете задать от 2 до 6 граней - и получите крутые фигуры! Сколько граней зададим? "))
colors = ["red", "yellow", "green", "blue", "orange", "purple"]
for x in range (360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
    t.left(90)