"""
# 1-1. 입력받은 금액의 단위별 지폐수 세기 ( 십만원, 만원, 천원 )
def 계산하기1(a):
    print("십만원 :", a // 100000, "장")
    print("만원 :", a // 10000, "장")
    print("천원 :", a // 1000, "장")

money1 = int(input("금액 : "))
계산하기1(money1)

# 1-2. 입력받은 금액을 입력받은 지폐로 나눠 지폐수 세기
def 계산하기2(a, b):
    print(a // b,"장")

money2 = int(input("금액 : "))
bill = int(input("지폐 단위 : "))
계산하기2(money2, bill)
"""

"""
# 2. 입력받은 값이 2의 배수인지 5의 배수인지 확인하기
def 분별하기(a):
    if a % 2 == 0 and a % 5 == 0:
        print("2와 5의 배수입니다")
    elif a % 2 == 0:
        print("2의 배수입니다")
    elif a % 5 == 0:
        print("5의 배수입니다")

num = int(input("숫자 : "))
분별하기(num)
"""

"""
# 3. 2명의 학생의 이름과 국어 성적과 영어성적을 입력받아 점수와 평균을 출력
def 평균구하기(a, b, c):
    print("========== 성적부 ==========")
    print("성명    국어    영어    평균")
    print(c,"",b,"   ",a,"   ",(a+b)/2)

English1 = int(input("첫 번째 학생의 영어성적 : "))
Korean1 = int(input("첫 번째 학생의 국어성적 : "))
name1 = input("첫 번째 학생의 이름 : ")
English2 = int(input("두 번째 학생의 영어성적 : "))
Korean2 = int(input("두 번째 학생의 국어성적 : "))
name2 = input("두 번째 학생의 이름 : ")
평균구하기(English1, Korean1, name1)
평균구하기(English2, Korean2, name2)
"""

"""
# 4. 2명의 학생의 이름과 1교시 2교시 3교시 비고 출력
    # 4-1. 출석 입력
name1 = input("첫 번째 학생의 이름 : ")
class11 = int(input("첫 번째 학생의 1교시(출석 : 1 결석 : 0) : "))
class12 = int(input("첫 번째 학생의 2교시(출석 : 1 결석 : 0) : "))
class13 = int(input("첫 번째 학생의 3교시(출석 : 1 결석 : 0) : "))
name2 = input("두 번째 학생의 이름 : ")
class21 = int(input("두 번째 학생의 1교시(출석 : 1 결석 : 0) : "))
class22 = int(input("두 번째 학생의 2교시(출석 : 1 결석 : 0) : "))
class23 = int(input("두 번째 학생의 3교시(출석 : 1 결석 : 0) : "))

    # 4-2. 비고 : 출석의 합
def 출석(a, b, c, d):
    print("============= 출석부 =============")
    print("성명    1교시    2교시    3교시    비고")
    print(d , " " , a , "    " , b , "      " , c , "     ", a + b + c)

    # 4-3. 출력
출석(class11, class12, class13, name1)
출석(class21, class22, class23, name2)
"""