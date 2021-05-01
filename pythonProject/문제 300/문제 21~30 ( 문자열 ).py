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