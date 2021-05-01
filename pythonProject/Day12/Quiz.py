"""
# 1. "비트코인" 문자열을 화면에 출력하면 print_coin() 함수를 정의해라.
def print_coin():
    print("비트코인")
"""

"""
# 2. 1번에서 정의한 print_coin 함수를 호출해라
print_coin()
"""

"""
# 3. 1번에서 정의한 print_coin을 100번 호출해라
for i in range(100):
    print_coin()
"""

"""
# 4. "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의해라.
def print_coins():
    for i in range(100):
        print("비트코인")
"""

"""
# 5. 아래에서 에러가 발생하는 이유에 대해 설명해라
hello()
def hello():
    print("HI")

# 정의가 된후 실행을 해야 하는데 정의가 안 된 상태에서 실행한후 정의를 해서
"""

"""
# 6. 아래 코드의 실행 결과를 예측해라
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
"""

"""
# 7. 아래 코드의 실행 결과를 예측해라.
print("A")

def message() :
    print("B")
    
print("C")
message()

# A
# C
# B
"""

"""
# 8. 아래 코드의 실행 결과를 예측해라.
print("A")
def message1():
    print(("B"))
print("C")
def message2():
    print("D")
message1()
print("E")
message2()

# A
# C
# B
# E
# D
"""

"""
# 9. 아래 코드의 실행 결과를 예측해라.
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

# B
# A
"""

"""
# 10. 아래 코드의 실행 결과를 예측해라.
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
"""

"""
# 11. 함수의 호출 결과를 예측해라.
def 함수(문자열):
    print(문자열)

함수("안녕")
함수("Hi")

# 안녕
# Hi
"""

"""
# 12. 함수의 호출 결과를 예측해라.
def 함수(a,b):
    print(a + b)
    
함수(3,4)
함수(7,8)
"""

"""
# 13. 아래와 같은 에러가 발생하는 원인을 설명해라
def 함수(문자열):
    print(문자열)
    
함수()

# 함수()여기서 괄호안에 문자열이 있어야 출력이 가능하고 실행이 가능한데 없어서
"""

"""
# 14. 아래와 같은 에러가 발생하는 원인을 설명해라
def 함수(a,b):
    print(a + b)
    
함수("안녕", 3)

# 더하기를 할려면 int형 이여야 하는데 "안녕"은 str이여서
"""

"""
# 15. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의해라.
def print_with_smile(str):
    print(str, ":D")

# 16. 15번에서 정의한 함수를 호출해라. 파라미터는 안녕하세요로 입력해라.
print_with_smile("안녕하세요")
"""

"""
# 17. 현재 가격을 입력 받아 상한가(30%)를 출력하는 print_upper_price 함수를 정의해라
def print_upper_price(int) :
    print(int + int * 0.3)
"""

"""
# 18. 두 개의 숫자를 입력받아 두 수의 함을 출력하는 print_sum 함수를 정의하라.
def print_sum(int1, int2):
    print(int1 + int2)
"""

"""
# 19. 두개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성해라.
def print_arithmetic_operation(int1,int2):
    print(int1 + int2)
    print(int1 - int2)
    print(int1 * int2)
    print(int1 / int2)
"""

"""
# 20. 세 개의 숫자를 입력받아 가장 큰 수를 출력하는 print_max 함수를 정의해라. 단 if문을 사용해서 수를 비교해라.
def print_max(int1,int2,int3):
    if int1 > int2:
        if int1 > int3:
            print(int1)
        else :
            print(int3)
    else :
        if int2 > int3:
            print(int2)
        else :
            print(int3)
"""

"""
# 21. 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의해라
def print_reverse(str):
    for a in reversed(str):
        print(a, end="")

print_reverse("abcd")
"""

"""
# 22. 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의해라.
def print_score(int1, int2, int3):
    print((int1 + int2 + int3) / 3)
"""

"""
# 23. 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even함수를 정의해라.
def print_even(list) :
    for i in list:
        if i % 2 == 0:
            print(i)
"""

"""
# 24. 하나의 딕셔너리를 입력받아 딕셔너리의 key값을 화면에 출력하는 print_keys 함수를 정의해라.
def print_keys(dictionary) :
    for i in dictionary.items():
        print(i[1])
"""

"""
# 25. my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장되어 있다.
my_dict = {"10/26": [100,130,100,100], "10/27":[10,12,10,11]}
# my_dict와 날짜 키값을 입력받아 ohlc리스트를 출력하는 print_value_by_key 함수를 정의해라.
def print_value_by_key(key, key_value):
    print(key[key_value])
"""

"""
# 26. 입력 문자열을 한 줄에 다섯 글자씩 출력하는 print_5xn함수를 작성해라
def print_5xn(str):
    for i in range(0,len(str)):
        if i % 5 == 0 :
            print("")
        print(str[i], end="")
"""

"""
# 27. 문자열과 한줄에 출력될 글자 수를 입력받아 한줄에 입력된 글자 수만큼 출력하는 print_max함수를 작성해라
def print_max(str, int):
    for i in range(0,len(str)):
        if i % int == 0 :
            print("")
        print(str[i], end="")
"""

"""
# 28. 연봉을 입력받아 월금을 계산하는 calc_monthly_salary 함수를 정의 해라.
def calc_monthly_salary(int) :
    print(int / 12 // 100000 * 100000)
"""

"""
# 29. 아래 코드의 실행 결과를 에측해라.
def my_print(a,b):
    print("왼쪽", a)
    print("오른쪽", b)

my_print(a = 100, b = 200)

# 왼쪽 100
# 오른쪽 200
"""

"""
# 30. 아래 코드의 실행 결과를 예측해라.
def my_print(a,b):
    print("왼쪽", a)
    print("오른쪽", b)

my_print(b = 100, a = 200)

# 왼쪽 200
# 오른쪽 100
"""

"""
# 31. 아래 코드의 실행 결과를 예측해라.
def n_plus_1 (n):
    result = n + 1
    
n_plus_1(3)
print(result)

# 오류가 걸린다.
"""

"""
# 32. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의해라.
def make_url(str) :
    print("www." + str + ".com")
"""

"""
# 33. 문자열 하나를 입력받아 각 문자들로 구성된 리스트로 반환 하는 make_list 함수를 정의해라.
list = []
def make_list(str):
    for i in range(0,len(str)):
        list.append(str[i])

make_list("list")
print(list)
"""

"""
# 34. 숫자로 구성된 하나의 리스트를 입력받아. 짝수를 추출하여 리스트로 변환하는 pickup_even 함수를 구현해라.
list2 = []
def pickup_even(list):
    for i in list:
        if i % 2== 0:
            list2.append(i)
            print(i, end=" ") 

pickup_even([2,5,6,3,4,5])
"""

"""
# 35. 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convrt_int 함수를 정의해라.
def convert_int(str1):
    str1 = str1.replace(".", "")
    print(int(str1))

convert_int("1.2345.234")
"""

"""
# 36. 아래 코드의 실행 결과를 예측해라.
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)

print(c)

# 22
"""

"""
# 37. 아래 코드의 실행 결과를 예측해라
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

# 22
"""

"""
# 38. 아래 코드의 실행 결과를 예측해라.
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

# 140
"""

"""
# 39. 아래 코드의 실행 결과를 예측해라.
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

# 16
"""

"""
# 40. 아래 코드의 실행 결과를 예측해라.
def 함수0(num):
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)

# 28
"""

"""
# 41. 현재 시간을 화면에 출력하시오
import datetime
print(datetime.datetime.now())
"""

"""
# 42. datetime 모듈의 now함수의 리턴 값의 타입을 화면에 출력하시오
import datetime
print(type(datetime.datetime.now()))
"""

"""
# 43, datetime 모듈의 timedelta를 사용해서 오늘로 부터 5일 4일 3일 2일 1일 전의 날짜를 화면에 출력해보세요
import datetime
for i in range(1,6):
    print(datetime.datetime.now() - datetime.timedelta(days=6 - i))
"""

"""
# 44. 현재 시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요
import datetime
now = datetime.datetime.now()
time = now.strftime("%Y %H:%M:%S")
print(time)
"""

"""
# 45. "2020-05-04"의 문자열을 시간 타입으로 변환해 보세요
import datetime
now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d")
print(time)
"""

"""
# 46. sleep 함수 time 모듈, data time 모듈을 사용해서 1초에 한 번 씩 현재 시간을 출력하는 코드를 작성하시오
while True:
    import time
    import datetime
    now = datetime.datetime.now()
    time2 = now.strftime("%Y %H:%M:%S")
    print(time2)
    time.sleep(1)
"""

"""
# 47. 모듈을 임포트를 하는 4가지 방식과 이유를 쓰시오
# 1. import 모듈
# 2. 모듈에 있는 코드들을 쓸려고
# 3. from 모듈 import 이름
# 4. 모듈안에 있는 특정한 코드 하나를 쓸려고
# 5. import 모듈 as 이름
# 6. 모듈을 불러오는데 이름을 이름으로 바꾸기
"""

"""
# 48. os 모듈의 getcwd 함수를 호출하면 현재 디렉터리의 경로를 화면에 출력해보세요
import os
print(os.environ['PATH'])
"""

"""
# 49. 바탕화면에 텍스트 파일 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요
import os
os.rename('C:\\Users\\User\\Desktop\\아무거나', 'C:\\Users\\User\\Desktop\\아무거나2')
"""

"""
# 50. numpy 모듈의 arange 함수를 사용해서 0.0부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요
import numpy
print(numpy.arange(0.0, 5.1, 0.1))
"""