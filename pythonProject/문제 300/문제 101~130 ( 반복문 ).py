# 101. 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
# bool

# 102. 아래 코드의 출력 결과를 예상하라
print(3 == 5)
# False

# 103. 아래 코드의 출력 결과를 에쌍하라
print(3 < 5)
# True

# 104. 아래 코드의 결과를 예상해라
x = 4
print(1 < x < 5)
# True

# 105. 아래 코드의 결과를 예상해라.
print((3 == 3) and (4 != 3))
# True

# 106. 아래 코드에서 에러가 발생하는 원윈에 대해 설명해라
# print(3 => 4)
# 저런 등위같은건 == != <= >= 밖에 없다

# 107. 아래 코드의 출력 려과를 예상해라
if 4 < 3:
    print("Hello World")
# 아무것도 출력이 안 됨

# 108. 아래 코드의 출력 결과를 예상해라.
if 4 < 3:
    print("Hellow World")
else :
    print("Hi, there")
# Hi, there

# 109. 아래 코드의 출력 결과를 예상해라.
if True :
    print("1")
    print("2")
else :
    print("3")
print("4")

# 110. 아래 코드의 출력 결과를 예상해라.
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")
# 3
# 5

# 111. 사용자로부터 입력받은 문자열을 두 번 출력해라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력한 결과이다.
answer = input("문자열을 입력하세요 : ")
print(answer * 2)

# 112. 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력해라.
answer = input("숫자를 입력하세요 : ")
print(int(answer) + 10)

# 113. 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별해라.
answer = input("숫자를 입력하세요 : ")
if int(answer) % 2 == 0:
    print("짝수입니다")
else :
    print("홀수입니다")

# 114. 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력해라. 단 사용자가 입력한 값과 20을 더한 계산 값이
# 255를 초과하는 경우 255를 출력해야 한다.
answer = input("숫자를 입력하세요 : ")
if int(answer) + 20 > 255 :
    print(255)
else :
    print(int(answer) + 20)

# 115. 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력해라. 단 출력 값의 범위는 0 ~ 255이다. 예를 들어
# 결과값이 0보다 작은 값이 되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255을 출력해야 한다.
answer = input("숫자를 입력하세요 : ")
if int(answer) - 20 > 255 :
    print(255)
elif int(answer) - 20 < 0 :
    print(0)
else :
    print(int(answer) - 20)

# 116. 사용자로부터 입력 받은 시간이 정각인지 판별해라.
answer = input("현재 시간 : ")
answer = answer.replace(' ','')
answer = answer.split(':')
if answer[1] == '00':
    print('정각입니다')
else :
    print("정각이 아닙니다")

# 117. 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우
# "오답입니다"를 출력해라
fruit = ["사과","포도","홍시"]
answer = input("좋아하는 과일은? ")
if answer in fruit:
    print("정답입니다")
else :
    print("오답입니다.")

# 118. 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고
# 종목입니다'를 아니면 "투자 경고 종목이 아닙니다"를 출력하는 프로그램을 작성해라.
warn_investment_list = ["Microsoft","Google","Naver","KaKao","SAMSUNG","LG"]
answer = input("투자할 종목을 입력하세요 : ")
if answer in warn_investment_list:
    print("투자 경고 종목입니다")
else :
    print("투자 경고 종목이 아닙니다.")

# 119. 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"
# 를 아닐 경우 "오답입니다"를 출력해라.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
answer = input("가장 좋아하는 계절은? ")
if answer in fruit:
    print("정답입니다")
else :
    print("오답입니다")

# 120. 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값에 포함되었다면 "정답입니다"
# 를 아닐 경우 "오답입니다"를 출력해라.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
answer = input("가장 좋아하는 과일은? ")
if answer in fruit.values():
    print("정답입니다.")
else :
    print("오답입니다.")

# 121. 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력해라.
answer = input("문자 한 개를 입력하세요 : ")
if answer.islower :
    answer = answer.upper()
elif answer.isupper() :
    answer = answer.lower()
print(answer)

# 122. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score을 입력받아 학점을 출력해라
score = input("점수를 입력하세요 : ")
if int(score) >= 81:
    print("A")
elif int(score) >= 61:
    print("B")
elif int(score) >= 41:
    print("C")
elif int(score) >= 21:
    print("D")
else :
    print("E")

# 123. 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성해라. 각 통화별
# 환율은 다음과 같다. 사용자는 100달러, 1000 엔, 13 유로, 100위안 같이 금액과 통화명 사이에 공백을 넣어 입력
# 한다고 가정한다.
money = input("돈을 입력하세요 : ")
money = money.split(' ')
if money[1] == "엔":
    print(int(money[0]) * 1.096,"원")
elif money[1] == "유로":
    print(int(money[0]) * 1268, "원")
elif money[1] == "달러":
    print(int(money[0]) * 1167, "원")
elif money[1] == "위안":
    print(int(money[0]) * 171, "원")

# 124. 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력해라.
number1 = int(input("숫자를 입력하세요 : "))
number2 = int(input("숫자를 입력하세요 : "))
number3 = int(input("숫자를 입력하세요 : "))
numbers = []
numbers.append(number1)
numbers.append(number2)
numbers.append(number3)
numbers = sorted(numbers, reverse=True)
for i in numbers:
    print(i)

# 125. 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사요자로부터 휴대전화 번호를 입력 받고 통신사를 출력
# 하는 프로그램을 작성해라.
answer = input("전화번호를 입력하세요(-넣고) ")
answer = answer.split('-')
if answer[0] == '011':
    print("SKT")
elif answer[0] == '016':
    print("KT")
elif answer[0] == '019':
    print("LGU")
elif answer[0] == '010':
    print("알수없음")

# 126. 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를 들어, 강북구의 경우 010,011,012 세 자리로
# 시작한다.
answer = input("우편 번호를 입력하시오 : ")
if answer[2] == 0 or 1 or 2:
    print("강북구")
elif answer[2] == 3 or 4 or 5:
    print("도봉구")
elif answer[2] == 6 or 7 or 8 or 9 :
    print("노원구")

# 127. 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 주민 등록 번호를 입력 받은 후 출생지가
# 서울인지 아닌지 판단하는 코드를 작성해라.
answer = input("주민등록 번호 : ")
answer = answer.split('-')
if answer[1][0] == '1' or '3' :
    print("남자입니다")
elif answer[1][0] == '2' or '4' :
    print("여자입니다")

# 128. 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 주민 등록 번호를 입력 받은 후 출생지가
# 서울인지 아닌지 판단하는 코드를 작성해라
answer = input("주민등록 번호 : ")
answer = answer.split('-')
if answer[1][1] == '0' and int(answer[1][2]) <= 8 :
    print("출생지는 서울입니다")
elif answer[1][1] == '0' and int(answer[1][2]) >= 9 :
    print("출생지가 서울이 아닙니다")

# 129. 주민등록 번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사요된다. 먼저 앞에서부터
# 12자리의 숫자에 2,3,4,5,6,7,8,9,2,3,4,5를 차례로 곱한 뒤 그 값을 전부 더한다. 연산 결과 값을 11로 나누면 나머지가
# 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.
answer = input("주민등록 번호 : ")
answer = answer.replace('-','')
last_number = 0
a = 2
b = 0
for i in answer:
    if a == 10:
        a = 2
        b = 1
    if b == 1 and a == 6:
        break
    last_number += int(i) * a
    a += 1
print(last_number)
last_number = last_number % 11
print(last_number)
last_number = 11 - last_number
print(last_number)
if int(answer[len(answer) - 1]) == last_number:
    print("유효하는 주민등록번호입니다")
else :
    print("유효하지 않는 주민등록번호입니다")

# 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
if int(btc['opening_price']) + int(btc['max_price']) - int(btc['min_price']) > int(btc['max_price']):
    print("상승장")
else :
    print("하락장")