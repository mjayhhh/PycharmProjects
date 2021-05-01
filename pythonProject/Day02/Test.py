"""
입출력
    1. 출력 print( 출력하고 싶은 데이터 )
    2. 입력 input() : 입력받기 [ 문자로 입력받음 ]
        -> int(input()) 로 int형으로 변경 가능
    3. 변수[저장소/변하는값] <----> 상수[저장소/고정값]


# 1. 입력받기
input("이름 : ")

# 2. 입력받은 값을 변수에 저장 & 출력
이름 = input("이름 : ")
print("당신의 이름 : " + 이름)

# 3. 출력 코드에 입력받고 받은 값을 출력
print("이름 : " + input("이름 : "))

# 4.입력받은 원의 색상과 크기를 터틀에 적용
color = input("원의 색상 : ")
size = int(input("원의 크기 : "))

import turtle
t = turtle.Turtle()

t.shape("turtle")
t.color(color)
t.begin_fill()
t.circle(size)
t.end_fill()

turtle.mainloop()
"""

# 5. 거북이[플레이어] 생성하기
import turtle

플레이어 = turtle.Turtle()
플레이어.color("blue")
플레이어.shape("turtle")
플레이어.penup()
플레이어.speed(0)
screen = 플레이어.getscreen()

# 6. 랜덤 인수(빨간 원 10개를 랜덤 위치에 만들기)

import  random
from builtins import range

마스테로이드 = []

for i in range(10):
    a1 = turtle.Turtle()
    a1.shape("circle")
    a1.color("red")
    a1.penup()
    a1.speed(0)
    a1.goto(random.randint(-300, 300), random.randint(-300,300))

    마스테로이드.append(a1)

# 7. 거북이 움직이기
def 전진():
    플레이어.forward(30)
def 후진():
    플레이어.forward(-30)
def 왼쪽회전():
    플레이어.left(30)
def 오른쪽회전():
    플레이어.right(30)
def 플레이():

    for a in 마스테로이드:    # a가 마스테로이드 리스트에 저장된 갯수만큼 반복
        a.right(random.randint(-180,180))
        a.forward(5) # 빨간색 점 5만큼 이동

        if 플레이어.distance(a) < 20:
            플레이어.write("+1")
            a.setx(1000)

    screen.ontimer(플레이, 10)
screen.ontimer(플레이, 10)
screen.onkeypress(전진, "Up")
screen.onkeypress(후진, "Down")
screen.onkeypress(오른쪽회전, "Right")
screen.onkeypress(왼쪽회전, "Left")
screen.listen()

turtle.mainloop()
