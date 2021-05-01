"""
문법 정리

문법 : 명령어

출력어 : print()

입력어 : input() # 이때 숫자를 써도 문자열로 저장됨
    int형으로 할려면 int( input() )

변수 : 어떠한 값을 저장하는 상자

산술 연산자 : +, -, /, *, **(제곱), %(나머지), //(몫)

비교 연산자 : >, >=, <, <=, ==, !=

논리 연산자 :
            and : 모두 다 참이여야 True 아니면 False
            or  : 둘 중 하나면 True이면 True
            not : True이면 False, False이면 True를 반환 함
제어문 : if
if 조건 :
    참일때의 실행할 코드
elif 조건 : ( 여러개의 조건을 입력 할때 씀)
    참일때의 실행할 코드
else :
    거짓일때의 실행할 코드

복합 대입 연산자 : 계산 후에 대입기호
    a = a + b       # a += b
    a = a - b       # a -= b
    a = a * b       # a *= b
    a = a / b       # a /= b 등

반복문 :
    while 조건 # 조건이 True일 때 동안 반복

    for i in range(a) # a번 만큼 반복

    for i in range(a, b) # a부터 b까지 1씩 더하면서 i변수에 대입
"""
if 10 > 5 :
    print("10이 더 큽니다.")
else :
    print("5가 더 큽니다")

# 1~100까지의 누적 합계
num = 0
for i in range(1, 100):
    num += i
print(num)

# 5번) 반복 실행
for i in range(5):
    print("반복")