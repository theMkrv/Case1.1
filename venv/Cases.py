#case 1
import turtle

# case 1
# Вместо того , чтобы каждый раз прописывать turtle пишете t (вызвали как t)
import turtle as t
import math
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
    t.seth(315)
    triangle90(198, -302, 30, "purple")
    t.seth(45)
    square(200, -300, 30, "orange")
    t.seth(135)
    triangle90(269, -322, 65, "red")
    t.seth(-45)
    paralellogramm(272, -325, 30, "green")
    t.seth(315)
    triangle90(-322, -176, 65, "yellow")


    t.seth(0)
    paralellogramm(-340, -302, 30, "green")
    t.seth(225)
    triangle90(-275, -270, 45, "blue")
    t.seth(45)
    triangle90(-318, -268, 30, "pink")
    t.seth(45)
    square(-295, -246, 30, "orange")
    t.seth(315)
    triangle90(-322, -176, 65, "red")
    t.seth(270)
    triangle90(-325, -200, 65, "yellow")
    triangle90(-292, -170, 30, "purple")



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
    paralellogramm(-12, -202, 30, "green")



    t.seth(90)
    triangle90(-350, 220, 50, "yellow")
    t.seth(270)
    triangle90(-319, 248, 30, "blue")
    triangle90(-296, 218, 20, "purple")
    t.seth(270)
    triangle90(-300, 324, 50, "red")
    t.seth(0)
    square(-297, 341, 30, "orange")
    paralellogramm(-310, 345, 25, "green")
    t.seth(90)
    ravb(-297, 300, 25, "pink")
    t.seth(0)
    triangle90(-50, 380, 70, "red")
    t.seth(270)
    triangle90(20, 307, 70, "yellow")
    t.seth(90)
    triangle90(24, 258, 50, "blue")
    t.seth(180)
    triangle90(74, 308, 50, "blue")
    t.seth(45)
    square(-42, 310, 40, "orange")
    t.seth(0)
    paralellogramm(-81, 310, 35, "green")
    t.seth(90)
    triangle90(-81, 272, 35, "pink")
    t.seth(270)
    triangle90(-83, 307, 35, "purple")
    t.seth(90)
    triangle90(290, 230, 70, "yellow")
    t.seth(270)
    triangle90(343, 277, 25, "purple")
    t.seth(0)
    triangle90(318, 252, 25, "purple")
    t.seth(0)
    triangle90(218, 340, 70, "red")
    t.seth(180)
    triangle90(288, 342, 35, "blue")
    t.seth(270)
    triangle90(253, 377, 35, "blue")
    square(360, 304, 30, "orange")
    t.seth(270)
    triangle90(360, 354, 20, "pink")
    triangle90(380, 334, 20, "pink")


    t.exitonclick()
    t.mainloop()


main()