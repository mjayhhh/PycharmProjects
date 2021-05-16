# 201. "비트코인" 문자열을 출력하는 print_coin() 함수를 정의하시오.
def print_coin():
    print("비트코인")

# 202. 201에서 정의한 함수를 호출하시오
print_coin()

# 203. 201에서 정의한 함수를 100번 호출하시오
for i in range(100):
    print_coin()

# 204. "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의해라.
def print_coins() :
    for i in range(100):
        print("비트코인")

# 205. 아래의 에러가 발생하는 이유에 대해 설명해라.
# hello()
# def hellow():
#     print("Hi")
#
# NameError: name 'hello' is not defined

# hellow 함수를 정의한 후에 사용해야 하는데 사용한 후에 정의를 해서

# 206. 아래 코드의 실행 결과를 예측해라.
def message():
    print("A")
    print("B")

message()
print("C")
message()

# A
# B
# C
# A
# B

# 207. 아래 코드의 실행 결과를 예측해라.
print("A")

def message() :
    print("B")

print("C")
message()

# A
# C
# B

# 208. 아래 코드의 실행 결과를 예측해라.
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()
# A
# C
# B
# E
# D

# 209. 아래 코드의 실행 결과를 예측해라.
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

# B
# A

# 210. 아래 코드의 실행 결과를 예측해라.
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range(3):
        message2()
        print("C")
    message1()

message3()

# B
# C
# B
# C
# B
# C
# A

# 211. 함수 호출 결과를 예측해라.
def 함수(문자열):
    print(문자열)

함수("안녕")
함수("Hi")

# 안녕
# Hi

# 212. 함수의 호출 결과를 예측해라.
def 함수(a, b) :
    print(a + b)

함수(3, 7)
함수(7, 8)

# 10
# 15

# 213. 아래와 같은 에러가 발생하는 원인을 설명해라.
# def 함수(문자열):
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'

# 함수 정의할때 입력값이 필요하다고 설정했는데 입력값을 안 넣어서

# 214. 아래와 같은 에러가 발생하는 원인을 설명해라.
# def 함수(a,b):
#     print(a + b)
#
# 함수("안녕",3)
# TypeError: can only concatenate str (not "int") to str

# 위와 같은 함수를 실행 시킬려면 같은 문자열이나 정수형식이 되야하므로 정수형식과 문자형식을 같이 넣었으니 에러가 걸린다

# 215. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의해라.
def print_with_smile(문자열):
    print(문자열, ":D")

# 216. 215에서 정의한 함수를 호출해라. 파라미터는 "안녕하세요"로 입력해라.
print_with_smile("안녕하세요")

# 217. 현재 가격을 입력 받아 상한가(30%)를 출력하는 print_upper_price 함수를 정의해라.
def print_upper_price(정수):
    print(정수 + 정수 * 0.3)

print_upper_price(100)

# 218. 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의해라.
def print_sum (정수1,정수2):
    print(정수1 + 정수2)

print_sum(7,3)

# 219. 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성해라.
def print_arithmetic_operation(x, y):
    print(x, "+", y, "=", x + y)
    print(x, "-", y, "=", x - y)
    print(x, "*", y, "=", x * y)
    print(x, "/", y, "=", x / y)

print_arithmetic_operation(3,4)

# 220. 세 개의 숫자를 입력받아 가장 큰 수를 출력하는 print_max 함수를 정의해라. 단 if문을 사용해서 수를 비교해라.
def print_max():
    num1 = input("숫자를 입력하세요 : ")
    num2 = input("숫자를 입력하세요 : ")
    num3 = input("숫자를 입력하세요 : ")
    if num1 > num2 :
        if num1 > num3 :
            print(num1)
        else :
            print(num3)
    else :
        if num2 > num3 :
           print(num2)
        else :
            print(num3)

# 221. 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의해라.
def print_reverse(x):
    for i in range(len(x)):
        print(x[len(x) - i - 1], end='')
    print()

print_reverse("python")

# 222. 성적 리스트를 입력 받아 평균을 출력 하는 print_score 함수를 정의해라
def print_score(num1,num2,num3):
    print((num1 + num2 + num3) / 3,"점")

print_score(1, 2, 3)

# 223. 하나의 리스트를 입력받아 짝수만 화면에 추력하는 print_even 함수를 정의해라
def print_even(list):
    for i in list:
        if i % 2 == 0:
            print(i)

print_even([1, 3, 2, 10, 12, 11, 15])

# 224. 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의해라
def print_keys(dictionary):
    for i in dictionary.keys():
        print(i)

print_keys({"이름":"김말똥","나이":30,"성별":"남"})

# 225. my_dict에는 날짜를 키값으로 OHLC 리스트가 저장되어 있다.
my_dict = {"10/26" : [100, 130, 100, 100], "10/27": [10,12,10,11]}
# my_dict 와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의해라
def print_value_by_key(dictionary, key):
    for i in dictionary[key]:
        print(i, end=' ')
    print()

print_value_by_key(my_dict, "10/26")

# 226. 입력 문자열을 한 줄에 다섯 글자씩 출력하는 print_5xn(string) 함수를 작성해라.
def print_5xn(string) :
    for i in range(0, len(string)):
        if i % 5 == 0 :
            print()
        print(string[i],end='')

print_5xn("아이엠어보이유알어걸")

# 227. 문자열과 하눚ㄹ에 출력될 글자수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작
# 성해라.
def printmxn(string, int) :
    for i in range(0, len(string)):
        if i % int == 0 :
            print()
        print(string[i],end='')
    print()

printmxn("아이엠어보이유알어걸", 3)

# 228. 연봉을 입력받아 월급을 계산하는 calc_monthly_salarty(annual_salarty) 함수를 정의해라. 회사는 연봉을 12개월로
# 나누어 분할 지금하면, 이 때 1원 미만은 버림한다.
def calc_monthly_salarty(annual_salarty):
    print(annual_salarty / 12)

calc_monthly_salarty(12000000)

# 229. 아래 코드의 실행 결과를 예측해라.
def my_print(a, b):
    print("왼쪽 :", a)
    print("오른쪽 :", b)

my_print(a = 100, b = 200)

# 왼쪽 : 100
# 오른쪽 : 200

# 230. 아래 코드의 실행 결과를 예측해라.
def my_print(a, b):
    print("왼쪽 :", a)
    print("오른쪽 :", b)

my_print(b = 100, a = 200)

# 왼쪽 : 200
# 오른쪽 : 100

# 231. 아래 코드를 실행한 결과를 예상해라.
# def n_plus_1(n):
#     result = n + 1
#
# n_plus_1(3)
# print(result)

# 오류가 걸린다. 왜냐 result n_plus_1 함수 정의 안에서 정의한 지역변수인데 밖에서 써서 그렇다.

# 232. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의해라.
def make_url(string):
    print("www."+string+".com")

make_url("naver")

# 233. 문자열을 입력받아 각 문자들로 구성된 리스트로 바노한하는 make_list 함수를 정의해라
def make_list(string):
    a = []
    for i in string:
        a.append(i)
    print(a)

make_list("abcd")

# 234. 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 하무슬ㄹ 구현하라.
def pickup_even(list):
    a = []
    for i in list :
        if i % 2 == 0 :
            a.append(i)
    print(a)

pickup_even([3, 4, 5, 6, 7, 8])

# 235. 코마가 포함된 문자열 수자를 입력받아 정수로 변환하는 convert_int 함수를 정의해라.
def convert_int(string):
    string = string.replace(',','')
    string = int(string)
    print(int(string))
    return string

convert_int("1,234,567")

# 236. 아래코드의 실행 결과를 예측해라.
def 함수(num):
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

# 22

# 237. 아래 코드의 실행 결과를 예측해라.
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

# 22

# 238. 아래 코드의 실행 결과를 에츠개할.
def 함수1(num):
    return num + 4

def 함수2(num):
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

# 140

# 239. 아래 코드의 실행 결과를 예측해라.
def 함수1(num):
    return num + 4

def 함수2(num):
    num += 2
    return 함수1(num)

c = 함수2(10)
print(c)

# 16

# 240. 아래 코드의 실행 결과를 예측해라.
def 함수0(num):
    return num * 2

def 함수1(num):
    return 함수0(num + 2)

def 함수2(num):
    num += 10
    return 함수1(num)

c = 함수2(2)
print(c)

# 28

# 반복문 = 기준에 따른 반복
    # 1. for 변수명 in 리스트명 : 리스트 값을 하나씩 변수명에 대입
    # 2. for 변수명 in range(시작값, 끝값, 증감단위) : 시작값부터 끝값까지 증감단위로 더하면서 변수명에 대입
        # range(값) : 값만큼 반복
        # range(시작값, 끝값) : 시작값부터 끝값까지 1씩 더하면서 반복

# 2 ~ 9단 구구단
for i in range(2,10): # 2부터 10까지 1씩 더하면서 반복
    print("=====",i,"단 =====")
    for a in range(1,10): # 1부터 10까지 1씩 더하면서 반복
        print(i,"X",a,"=",a * i)

# 피라미드 만들기
for n in range(0,5): # 0부터 5까지 1씩 더하면서 반복
    print(" " * (4 - n), end='')
    print("*" * (n * 2 + 1), end='')
    print("")

#     *
#    ***
#   *****
#  *******
# *********

