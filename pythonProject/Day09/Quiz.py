"""
# 1. 사용자로부터 입력받은 문자열을 두 번 출력하라.
answer = input("문자열을 입력하시오.\t") # answer에 입력받은 문자를 저장
print(answer * 2) # 문자 * 2 -> 문자 2번 출력
"""

"""
# 2. 사용자로부터 하나의 숫자를 입력받고 입력받은 숫자에 10을 더해 출력해라.
answer = int(input("숫자를 입력하시오.\t")) # answer에 int형으로 입력받은 숫자를 저장
print(answer + 10) # answer에 10을 더한 후 출력
"""

"""
# 3. 사용자로부터 하나의 숫자를 입력받고 짝수/홀수를 판별하라 
answer = int(input("숫자를 입력하시오.\t")) # answer에 int형으로 입력받은 숫자를 저장
if answer % 2 == 0: # 만약 answer / 2의 나머지가 0이면
    print("짝수입니다")
else: # 만약 answer / 2의 나머지가 0이 아니라면
    print("홀수입니다")
"""

"""
# 4. 사용자로부터 값을 입력받고 해당값에 20을 더한 값을 출력해라. 단 값이 255를 넘으면 255를 출력해야한다.
answer = int(input("숫자를 입력하시오.\t")) # answer에 int형을 입력받은 숫자를 저장
if answer + 20 > 255 : # 만약 answer + 20의 값이 255를 넘는다면
    print(255)
else :
    print(answer + 20) # 만약 answer + 20의 값이 255를 넘지 않는다면
"""

"""
# 5. 사용자로부터 값을 입력받고 해당값에 20을 뺀 값을 출력해라. 단 출력 값에 범위는 0~255까지이다.
answer = int(input("숫자를 입력하시오.\t")) # answer에 int형으로 입력받은 숫자를 저장
if answer - 20 < 0 : # 만약 answer - 20이 0보다 작으면
    print(0)
elif answer - 20 > 255: # 만약 answer - 20이 255보다 크면
    print(255)
else :
    print(answer - 20)
"""

"""
# 6. 사용자로부터 입력받은 시간이 정각인지 판별하라.
answer = []
answer = input("현재 시각을 입력하시오.\t") # answer에 입력 받은 값을 0부터 차례로 저장
if int(answer[2]) == 0: # 만약 answer[2] 의 값이 0 이라면
    if int(answer[3]) == 0: # 만약 answer[3]의 값이 0 이라면
        print("정각입니다")
else : # 만약 answer[2]와[3]의 값이 0이 아니라면
    print("정각이 아닙니다")
"""

"""
# 7. 사용자로부터 입력받은 단어가 fruit 리스트에 포함되어 있는지를 확인하라. 포함되어 있다면 "정답입니다" 아닐 경우 "오답입니다"를 출력해라
fruit = ["사과","포도","홍시"]
answer = input("좋아하는 과일은?\t") # answer에 입력받은 값을 저장
if answer in fruit:
    print("정답입니다.")
else :
    print("오답입니다.")
"""

"""
# 8. 사용자로부터 입력받은 단어가 투자 경고 종목 리스트에 있을 때 사용자로부터 '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하시오.
warn_investment_list = ["Microsoft", "Google", "Naver", "KaKao", "SAMSUNG", "LG"]
answer = input("투자할 회사를 입력하시오.\t")
if answer in warn_investment_list:
    print("투자 경고 종목입니다.")
else :
    print("투자 경고 종목이 아닙니다.")
"""

"""
# 9. 사용자가 입력한 값이 딕셔너리 키 값에 포함되어 있다면 "정답입니다" 아니면 "오답입니다"를 출력해라
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
answer = input("좋아하는 계절을 입력하시오.\t")
if answer in fruit:
    print("정답입니다.")
else:
    "오답입니다."
"""

"""
# 10. 사용자가 입력한 값이 딕셔너리 값에 포함되어 있다면 "정답입니다" 아닐 경우 "오답입니다"를 출력하라
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
answer = input("좋아하는 과일을 입력하시오.\t")
if answer in fruit.values():
    print("정답입니다.")
else :
    print("오답입니다.")
"""

"""
# 11. 사용자로부터 문자 한 개를 입력받고 소문자일 경우 대문자로, 대문자일 경우 소문자로 변경해서 출력
answer = []
answer = input("문자를 입력하시오.\t")
a = len(answer)
for i in range (0, a):
    if answer[i].islower():
        print(answer[i].upper() , end='')
    else :
        print(answer[i].lower(), end='')
"""

"""
# 12. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 socre를 입력받아 학점을 출력하라
answer = int(input("점수를 입력하시오.\t"))
if answer >= 81:
    print("A")
elif answer >= 61:
    print("B")
elif answer >= 41:
    print("C")
elif answer >= 21:
    print("D")
else :
    print("E")
"""

"""
# 13. 사용자로부터 달러, 엔 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변화하는 프로그램을 작성하라.
단위 = input("돈의 통화 : ")
돈 = int(input("알고싶은 통화의 돈의 양 : "))
if 단위 == "달러":
    print(돈 * 1167,"원")
elif 단위 == "엔":
    print(돈 * 1.096,"원")
elif 단위 == "유로":
    print(돈 * 1268,"원")
elif 단위 == "위안":
    print(돈 * 171, "원")
"""

"""
# 14. 사용자로부터 숫자 3개를 입력 받은 후 가장 큰 숫자를 입 출력 하라
answer = []
for i in range (3):
    answer.append(int(input("숫자를 입력하시오.\t")))
answer.sort()
print("가장 작은 숫자 :", answer[0])
print("가장 큰 숫자 :",answer[2])
"""

"""
# 15. 사용자로부터 휴대전화 번호를 입력받고, 통신사를 출력하는 프로그램을 작성하라.
answer = []
answer = input("휴대폰 번호 앞자리를 입력하시오.\t")
if int(answer[2]) == 1:
    print("통신사 : SKT")
elif int(answer[2]) == 6:
    print("통신사 : KT")
elif int(answer[2]) == 9:
    print("통신사 : LGU")
else :
    print("통신사 : 알수없음")
"""

"""
# 16. 사용자로부터 5자리 우편번호를 입력받고 구를 판별하라
answer = []
answer = input("우편번호를 입력하시오.\t")
if int(answer[2]) == 1 or int(answer[2]) == 0 or int(answer[2]) == 2:
    print("강북구")
elif int(answer[2]) == 3 or int(answer[2]) == 4 or int(answer[2]) == 5:
    print("도봉구")
else:
    print("노원구")
"""

"""
# 17. 사용자로부터 주민등록번호를 입력받은 후 성별를 출력하는 프로그램을 작성하시오.
answer = input("주민 등록 번호를 입력하시오.\t")
if int(answer[0]) == 1 or 3:
    print("남자")
else :
    print("여자")
"""

"""
# 18. 사용자로부터 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드르 작성하라
answer = input("주민 등록 번호를 입력하시오.\t")
if int(answer[8]) == 0 and int(answer[9]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")
"""

"""
# 19. 주민 등록 번호를 입력받은 후 그 주민 등록 번호가 유효한지 안 한지 체크하시오."""
answer = input("주민 등록 번호를 입력하시오.\t")
a = 2
last_number = 0
for i in range(0,13):
    if i == 6:
        pass
    else:
        if a > 9:
            a = 2
        last_number += int(answer[i]) * a
        a += 1
if 11 - last_number % 11 == int(answer[13]):
    print("유효한 주민등록번호입니다")
else :
    print("유효하지 않는 주민등록번호입니다")

