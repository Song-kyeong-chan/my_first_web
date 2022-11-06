"""
    progrmmer : 송경찬
    Date : 2022.9.9
    File name : py3-r1 송경찬.py
    Description: 두개의 별 그리기
"""

import turtle as t
t.shape("turtle")
t.title("Forever JBNU !")


a = int(input("a별의 한변의 길이를 입력하세요: "))
b = int(input("b별의 한변의 길이를 입력하세요: "))

t.penup()


t.goto(-100,200)

t.pendown()

t.color("purple")
t.write("Forever JBNU !",font = ('Times New Roman',50,'bold'))

t.penup()

t.goto(-200,0)

t.pendown()
t.color("blue")

t.begin_fill()

for i in range(5):
    t.forward(a)
    t.right(144)

t.end_fill()

t.penup()

t.goto(200,0)

t.pendown()
t.color("orange")

t.begin_fill()
t.left(144)

for i in range(5):
    t.forward(b)
    t.right(144)

t.end_fill()

t.ht()
