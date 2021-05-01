# 계산기 만들기
    # 1. 화면 만들기
    # 2. 계산창 버튼 추가
    # 3. 버튼에 명령 추가하기
    # 4. 함수( 여러개의 코드 묶음 )
    # 5. 계산 창에 클릭된 값을 저장

import tkinter as tk
from tkinter import * # tkinter : UI[이미지]
from tkinter import ttk

operation = []
number_list = []

def button_pressed(value):
    if value == "AC":
        number.delete(0,"end")
        operation.clear()
        number_list.clear()
    else :
        number.insert("end", value) # end : 오른쪽 끝에 버튼 이름 추가

def solve(value) :
    number_list.append(float(number.get()))
    number.delete(0, "end")
    operation.append(value)

def point() :
    number.insert("end", ".")

def equal() :
    number_list.append(float(number.get()))
    print(number_list)
    print(operation)
    number.delete(0, "end")
    result = 0
    a = 0
    for i in range(len(number_list)):
        if len(number_list) > 2:
            if operation[a] == "+":
                result += number_list[i]
            elif operation[a] == "-":
                result -= number_list[i]
            elif operation[a] == "*":
                if result == 0:
                    result += 1
                result *= number_list[i]
            elif operation[a] == "/":
                if result == 0:
                    result = number_list[i]
                result /= number_list[i + 1]
            if a + 1 >= len(operation):
                a = 0
            else :
                a += 1
        else :
            if operation[0] == "+":
                result += number_list[i]
            elif operation[0] == "-":
                result -= number_list[i]
            elif operation[0] == "*":
                if result == 0:
                    result += 1
                result *= number_list[i]
            elif operation[0] == "/":
                if result == 0:
                    result = number_list[i]
                result /= number_list[i + 1]
                break
    if result % 1 == 0 :
        number.insert("end", round(result))
    else :
        number.insert("end", result)
    operation.clear()
    number_list.clear()

screen = Tk()                  # 화면 그래픽 가져오기
screen.title("계산기")          # 화면 이름

number = StringVar( screen, value='')

# 숫자 및 결과 표시창
number= tk.Entry(screen, textvariable = number, width=43)
number.grid(rowspan=1, columnspan=5) # columnspan 은 여러칸에 걸쳐서 표시함.
            # row : 행[가로] # column : 열[세로]

# button 9개 추가
button7 = tk.Button(screen, text="7",width = 7, height = 2,borderwidth=1, command=lambda: button_pressed('7'))
button7.grid(row=1, column=0)
button8 = tk.Button(screen, text="8",width = 7, height = 2,borderwidth=1, command=lambda: button_pressed('8'))
button8.grid(row=1, column=1)
button9 = tk.Button(screen, text="9",width = 7, height = 2,borderwidth=1, command=lambda: button_pressed('9'))
button9.grid(row=1, column=2)
# 나누기 버튼 -> math_button_pressed() 로 연결.
button_div = tk.Button(screen, text="/",width = 7, height = 2,borderwidth=1, command=lambda: solve('/'))
button_div.grid(row=1, column=3)
button_point = tk.Button(screen, text=".",width = 7, height = 2,borderwidth=1, command=lambda: point())
button_point.grid(row=1, column=4)

button4 = tk.Button(screen, text="4",width = 7, height = 2,borderwidth=1, command=lambda: button_pressed('4'))
button4.grid(row=2, column=0)
button5 = tk.Button(screen, text="5",width = 7, height = 2,borderwidth=1, command=lambda: button_pressed('5'))
button5.grid(row=2, column=1)
button6 = tk.Button(screen, text="6",width = 7, height = 2,borderwidth=1, command=lambda: button_pressed('6'))
button6.grid(row=2, column=2)
# 곱하기 버튼 -> math_button_pressed() 로 연결.
button_mult = tk.Button(screen, text="*",width = 7, height = 2,borderwidth=1, command=lambda: solve('*'))
button_mult.grid(row=2, column=3)

button1 = tk.Button(screen, text="1",width = 7, height = 2,borderwidth=1, command=lambda: button_pressed('1'))
button1.grid(row=3, column=0)
button2 = tk.Button(screen, text="2",width = 7, height = 2,borderwidth=1, command=lambda: button_pressed('2'))
button2.grid(row=3, column=1)
button3 = tk.Button(screen, text="3",width = 7, height = 2,borderwidth=1, command=lambda: button_pressed('3'))
button3.grid(row=3, column=2)
# 더하기 버튼 -> math_button_pressed() 로 연결.
button_add = tk.Button(screen, text="+",width = 7, height = 2,borderwidth=1, command=lambda: solve('+'))
button_add.grid(row=3, column=3)

button_ac = tk.Button(screen, text="AC",width = 7, height = 2,borderwidth=1, command = lambda:button_pressed('AC'))
button_ac.grid(row=4, column=0)
button0 = tk.Button(screen, text="0",width = 7, height = 2,borderwidth=1, command = lambda:button_pressed('0'))
button0.grid(row=4, column=1)
button_equal = tk.Button(screen, text="=",width = 7, height = 2,borderwidth=1, command = lambda:equal())
button_equal.grid(row=4, column=2)
button_sub = tk.Button(screen, text="-",width = 7, height = 2,borderwidth=1, command = lambda:solve('-'))
button_sub.grid(row=4, column=3)

screen.mainloop() # 화면 계속 실행하기