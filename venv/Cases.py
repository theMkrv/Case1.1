#case 1
import turtle

# case 1
# Вместо того , чтобы каждый раз прописывать turtle пишете t (вызвали как t)
import turtle as t
import math
t.setup(800, 800)

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
    t.left(135)
    t.forward(1.5*a)
    t.left(45)
    t.forward (a)
    t.left(135)
    t.forward(1.5*a)
    t.left(45)
    t.forward(a)
    t.end_fill()

# Вертим всем функцией - t.seth() устанавливаем значение 1 - 360
def main():
    t.seth(0)
    paralellogramm(-340, -302, 30, "green")
    t.seth(225)
    triangle90(-275, -270, 45, "blue")
    t.seth(45)
    triangle90(-318, -268, 30, "pink")
    t.seth(45)
    square(-295, -246, 31, "orange")
    t.seth(315)
    triangle90(-322, -176, 65, "red")
    t.seth(270)
    triangle90(-325, -190, 65, "yellow")
    triangle90(-292, -175, 30, "purple")

    t.seth(45)
    square(-150, -250, 30, "orange")
    t.seth(225)
    triangle90(-78, -265, 30, "pink")
    t.seth(45)
    triangle90(-95, -286, 30, "purple")
    t.seth(135)
    triangle90(-35, -300, 50, "yellow")
    t.seth(315)
    triangle90(-32, -228, 50, "red")
    t.seth(45)
    triangle90(-105, -225, 50, "blue")
    t.seth(225)
    paralellogramm(-10, -204, 30, "green")

    t.seth(315)
    triangle90(198, -302, 30, "purple")
    t.seth(45)
    square(200, -300, 30, "orange")
    t.seth(135)
    triangle90(269, -322, 65, "red")
    t.seth(-45)
    paralellogramm(272, -325, 30, "green")
    t.seth(315)
    triangle90(221, -181, 65, "yellow")
    t.seth(360)
    triangle90(225, -177, 45, "blue")
    t.seth(45)
    triangle90(225, -175, 30, "purple")


    t.exitonclick()
    t.mainloop()


main()