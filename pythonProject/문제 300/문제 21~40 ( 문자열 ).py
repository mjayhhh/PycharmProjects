# 21. letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요
letters = 'python'
print(letters[0],letters[2])

# 22. 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
print(license_plate[4],license_plate[5],license_plate[6],license_plate[7], sep='')

# 23. 아래의 문자열에서 '홀'만 출력하세요.
string = "홀짝홀짝홀짝"
for i in string:
    if i == "홀":
        print("홀",end='')
print("")

# 24. 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
string = list(string)
string.reverse()
for i in string:
    print(i, end='')
print("")

# 25. 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
phone_number = phone_number.replace("-"," ")
print(phone_number)

# 26. 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하시오
phone_number = phone_number.replace(" ","")
print(phone_number)

# 27. url에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = "http://sharebook.kr"
url = url.split(".")
print(url[len(url) - 1])

# 28. 아래 코드의 실행 결과를 예상해보세요
# lang = "python"
# lang[0] = "P"
# print(lang)
# 오류가 걸린다

# 29. 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
string = string.replace('a','A')
print(string)

# 30. 아래 코드의 실행 결과를 예상해보세요.
string = 'abcd'
string.replace('b','B')
print(string)
# abcd

# 31. 아래 코드의 실행 결과를 예상해보세요
a = "3"
b = "4"
print(a + b)

# 32. 아래 코드의 실행 결과를 에상해보세요.
print("Hi" * 3)
# HiHiHi

# 33. 화면에 '-'를 80개 출력하세요
print("-" * 80)

# 34. 변수에 다음과 같은 문자열이 바인딩 되어 있습니다
t1 = 'python'
t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요
# python java python java python java python java python java
for i in range(4):
    print(t1, t2, end=' ')
print("")

# 35. 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 :",name1,"나이 :",age1)
print("이름 :",name2,"나이 :",age2)

# 36. 문자열의 format() 메소드를 사용해서 35번 문제를 다시 풀어보세요
m1 = "이름 : {name1} 나이 : {age1}".format(name1="김민수",age1 = 10)
m2 = "이름 : {name2} 나이 : {age2}".format(name2="이철희",age2 = 13)
print(m1)
print(m2)

# 37. f-string을 사용하여 35번 문제를 다시 풀어보세요
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
M1 = f'이름 : {name1} 나이 : {age1}'
M2 = f'이름 : {name2} 나이 : {age2}'
print(M1)
print(M2)

# 38. 삼성 전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요
상장주식수 = "5,969,782,550"
상장주식수 = 상장주식수.replace(",","")
print(상장주식수)

# 39. 다음과 같은 문자열에서 2020/03만 출력하세요
분기 = "2020/03(E) (IFRS연결)"
분기 = 분기.split("(")
print(분기[0])

# 40. 문자열의 좌우의 공백이 있을 때 이를 제거해보세요
data = "   삼성전자   "
data = data.replace(" ","")
print(data)