문자상자 = "파이썬"
숫자상자 = 24

# 변수 출력
print("숫자상자[변수]의 내용물 ??? : ", 숫자상자)
print("문자상자[변수]의 내용물 ??? : ", 문자상자)

# 변수 변경
숫자상자 = 20
print("숫자상자의 변경후 내용물 ??? : ", 숫자상자)

# 변수 계산
숫자상자2 = 30
print("숫자상자 + 숫자상자2 : ",숫자상자2+ 숫자상자)

# 산술 연산자 : 연산시 사용되는 특수 문자
# + : 더하기, - : 빼기 , * : 곱하기, ** : 제곱, / : 나누기, // : 몫만 구하기, % : 나머지만 구하기

# 2의 배수인지 5의 배수인지 출력하기
def 분별하기(a):
    if a % 2 and a % 5 :
        print("2와 5의 배수입니다")
    elif a % 2 == 0:
        print("2의 배수입니다")
    elif a % 5 == 0:
        print("5의 배수입니다")

분별하기(32)

# 단위별 지폐수 계산하기
def 계산하기(a):
    print(a // 100000, "장")
    print(a % 100000 // 10000, "장")
    print(a % 10000 // 1000, "장")

계산하기(456789)