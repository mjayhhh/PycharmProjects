""" 컴퓨터한테 명령[ 코드 ]
     1. # : 주석, """ """ : 여러 줄 주석
     2. print("쓰고싶은말") : 출력
     3. import 파일 가져오기( 코드 호출 ) 
"""

import turtle

# 기본 설정
t = turtle.Turtle()
t.shape("turtle")
t.color("green")

"""
def 팔그리기(a):
    t.right(45)
    t.forward(100)
    t.forward(-100)
    t.right(90)
    t.forward(100)
    t.forward(-100)

def 다리그리기(a):
    t.left(45)
    t.forward(100)
    t.forward(-100)
    t.right(90)
    t.forward(100)
    t.forward(-100)

def 원그리기(a):
    t.speed(0)
    for i in range(180):
        t.forward(2)
        t.left(2)

def 사각형그리기(a):
    for k in range(4):
        t.forward(100)
        t.right(90)

def 이등변삼각형그리기(a):
    a.left(45)
    t.forward(75)
    t.right(90)
    t.forward(75)
    t.right(135)
    t.forward(100)

# 쫄라맨 그리기
원그리기(t)
t.speed(3)
팔그리기(t)
t.left(45)
t.forward(150)
다리그리기(t)

# 이동하기
t.color("white")
t.left(135)
t.forward(200)
t.color("green")

# 집 그리기
사각형그리기(t)
이등변삼각형그리기(t)
"""
t.hideturtle()

colors = [ "red", "purple" , "blue", "orange", "yellow", "green" ]
turtle.bgcolor("black")
t.speed(0)
t.width(3)
length = 10

while length < 500 :
    t.forward(length)
    t.pencolor(colors[length % 6])
    t.right(180)
    length += 1

screen = t.getscreen()

screen.listen()
screen.mainloop()