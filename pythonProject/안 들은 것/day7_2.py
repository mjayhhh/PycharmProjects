#출력하기

#1. print(   )  함수 사용
print("Hello World")

#2. 괄호 " " 안 에 문자 입력
print("Mary's cosmetics")

#3. " " 큰따옴표 출력시 ' ' 작은 따옴표 사용
print('신씨가 소리질렀다. "도둑이야"')

#4. 키보드 엔터 위에 (원화기호)
print("C:\windows")

#5.
print("안녕하세요\n만나서\t\t반갑습니다")
# \t : 들여쓰기[ 탭=tab ]
# \n : 줄바꿈 [ 엔터=enter ]

#6. , 연결 연산자 [ 문자사이 띄어쓰기 ]
print("오늘은","일요일")
# 오늘은일요일

#7. sep=";" [ 문자사이의 띄어쓰기 대신 ; 대체 ]
print("naver","kakao","sk","samsung",sep=";")

#8. sep="/" [ 문자사이의 띄어쓰기 대신 / 대체 ]
print("naver","kakao","sk","samsung",sep="/")

#9. print 함수는 자동 줄바꿈 => 자동 줄바꿈제거
print("first" , end="")
print("second")

#10. 큰 따옴표가 없으면 나누기 처리
print("5/3")
print(5/3)

#11. 바인딩 :  저장 = 대입
삼성전자 = 50000 # 삼성전자 변수에 5만원 저장
총평가금액 = 50000 * 10
print(총평가금액)

#12. 변수 생성
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print("시가총액 : ",시가총액 )
print("현재가 : ",현재가)
print("PER : ", PER)

#13. 문자 변수
s = "hello"
t = "python"
print( s+"!",t)

#14. 변수 계산
계산 = 2 + 2 * 3
print(계산)

#15. type 함수 [ 숫자(int) 문자(str) 판별 ]
a=128
print( type(a))

a="132"
print( type(a))

#16. 문자열 "720" => 숫자 변환    int( 변수 )
num_str = "720"
print("정수변환 : ", int(num_str) )

#17. 숫자열 100 => 문자 변환       str( 변수 )
num = 100
print("문자변환 : " , str( num) )

#18. 문자열 15.79 => 실수[소수점] 변환    float( 변수 )
data = "15.79"
print("실수변환 : ", float(data))

#19.
year = "2020"
print(  int( year ) -1 )
print(  int( year ) -2 )
print(  int( year ) -3 )

#20.
월 = 48584
총금액 = 월 * 36
print(총금액)







