#case 1
import turtle

# case 1
# Вместо того , чтобы каждый раз прописывать turtle пишете t (вызвали как t)
import turtle as t
t.setup(800, 800)
# whats my little bitch

# x - corner coordinate x
# y - corner coordinate y
# a - side of the triangle
def triangle90(x, y, a, color):
    t.up()
    t.color(color)
    t.setposition(x, y)
    t.down()
    t.begin_fill()
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.setposition(x, y)
    t.end_fill()

#Равнобедренный треуголник
def ravb(x, y, a, color):
    t.color(color)
    t.up()
    t.begin_fill()
    t.setposition(x, y)
    t.down()
    t.right(150)
    t.fd(a)
    t.right(60)
    t.fd(a)
    t.setposition(x, y)
    t.end_fill()

#Тупа квадрат - ничего более
def square(x, y, a,color):
    t.up()
    t.setposition(x, y)
    t.color(color)
    t.down()
    t.begin_fill()
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.end_fill()

def paralellogramm(x, y, a, color):
    t.up()
    t.setposition(x, y)
    t.color(color)
    t.down()
    t.begin_fill()
    t.forward(a)
    t.left(125)
    t.forward(1.5*a)
    t.left(55)
    t.forward (a)
    t.left(125)
    t.forward(1.5*a)
    t.left(55)
    t.forward(a)
    t.end_fill()

# Вертим всем функцией - t.seth() устанавливаем значение 1 - 360
def sayoga_zayac():
    t.seth(45)
    square(-745, -250, 100, "purple")
    t.seth(225)
    triangle90(-500, -295, 100, "yellow")
    t.seth(45)
    triangle90(-560, -365, 100, "blue")
    t.seth(135)
    triangle90(-340, -435, 200, "orange")
    t.seth(180)
    ravb(-320, 270, 40, "red")
    t.seth(270)
    triangle90(-320, 220, 40, "red")
    paralellogramm(0,0,50,"blue")


    t.exitonclick()
    t.mainloop()


sayoga_zayac()