"""
# 1. for문의 실행결과를 예측하라
과일 = ["사과","귤","수박"]
for 변수 in 과일:
    print(변수)
# 사과, 귤, 수박
"""

"""
# 2. for문의 실행 결과를 예측하라
과일 = ["사과","귤","수박"]
for 변수 in 과일:
    print("#####")
# ##### ##### #####
"""

"""
# 3. 다음 for문과 동일한 기능을 수행하는 코드를 작성하세요.
for 변수 in ["A","B","C"]:
    print(변수)

리스트 = ["A","B","C"]
for 변수 in 리스트:
    print(변수)
"""

"""
# 4. for문을 풀어서 동일한 동작을 하는 코드를 작성하라.
for 변수 in ["A","B","C"]:
    print("출력", 변수)

변수 = "A"
print("출력", 변수)
변수 = "B"
print("출력", 변수)
변수 = "C"
print("출력", 변수)
"""

"""
# 5. for문을 풀어서 동일한 동작을 하는 코드를 작성하라
for 변수 in ["A","B","C"]:
    b = 변수.lower()
    print("변환", b)

리스트 = ["A","B","C"]
a = 리스트[0].lower()
print("변환", a)
a = 리스트[1].lower()
print("변환", a)
a = 리스트[2].lower()
print("변환", a)
"""

"""
# 6. 다음 코드를 for문으로 작성하라
변수 = 10
print(변수)
변수 = 20
print(변수)
변수 = 30
print(변수)

for 변수 in [10,20,30]:
    print(변수)
"""

"""
# 7. 다음 코드를 for문으로 작성하라
print(10)
print(20)
print(30)

for i in [10,20,30]:
    print(i)
"""

"""
# 8. 다음 코드를 for문으로 작성하라
print(10)
print("-------")
print(20)
print("-------")
print(30)
print("-------")

for i in [10,20,30]:
    print(i)
    print("-------")
"""

"""
# 9. 다음 코드를 for문으로 작성하라
print("++++")
print(10)
print(20)
print(30)

for i in ["++++",10,20,30]:
    print(i)
"""

"""
# 10. 다음 코드를 for문으로 작성하라
print("-------")
print("-------")
print("-------")
print("-------")

for i in range (4):
    print("-------")
"""

"""
# 11. 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for문을 이용해서 화면에 출력하라. 단 부가세는 10원으로 가정 한다
리스트 = [100,200,300]
for i in 리스트:
    print(i + 10)
"""

"""
# 12. for문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라
리스트 = ["김밥","라면","튀김"]
# 오늘의 메뉴 : 김밥
# 오늘의 메뉴 : 라면
# 오늘의 메뉴 : 튀김
for i in 리스트:
    print("오늘의 메뉴 :", i)
"""

"""
# 13. 리스트에 주식 종목이름이 저장되어 있다
리스트 = ["SK하이닉스","삼성전자","LG전자"]
# 저장된 문자열의 길이를 다음과 같이 출력하라
# 6
# 4
# 4
for i in 리스트:
    print(len(i))
"""

"""
# 14. 리스트에는 동물이름이 문자열로 저장되어 있다
리스트 = ['dog','cat','parrot']
# 동물 이름과 글자수를 다음과 같이 출력하라
# dog 3
# cat 3
# parrot 6
for i in 리스트:
    print(i, len(i))
"""

"""
# 15. 리스트에 동물 이름이 저장되어 있다
리스트 = ['dog','cat','parrot']
# for문을 이용하여 동물 이름의 첫 글자만 출력하라
# d
# c
# p
for i in 리스트:
    print(i[0])
"""

"""
# 16. 리스트에는 세 개의 숫자가 바인딩 되어 있다
리스트 = [1,2,3]
# for문을 사용해서 다음과 같이 출력하라
# 3 x 1
# 3 x 2
# 3 x 3
for i in 리스트:
    print(3,"x",i)
"""

"""
# 17. 리스트에는 세 개의 숫자가 바인딩 되어 있다
리스트 = [1,2,3]
# for문을 사용해서 다음과 같이 출력해라
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
for i in 리스트:
    print(3,"x",i,"=", 3 * i)
"""

"""
# 18. 리스트에는 네 개의 문자열이 바인딩되어 있다
리스트 = ["가","나","다","라"]
# for문을 이용해서 다음과 같이 출력하라
# 나
# 다
# 라
for i in range(3):
    print(리스트[i+1])
"""

"""
# 19. 리스트에는 네 개의 문자열이 바인딩되어 있다
리스트 = ["가","나","다","라"]
# for문을 이용해서 다음과 같이 출력하라
# 가
# 다
for i in range(2):
    print(리스트[i * 2])
"""

"""
# 20. 리스트에는 네 개의 문자열이 바인딩되어 있다
리스트 = ["가","나","다","라"]
# for문을 이용해서 다음과 같이 출력하라
# 라
# 다
# 나
# 가
for i in reversed(리스트):
    print(i)
"""

"""
# 21. 리스트에는 네 개의 정수가 저장되어 있다
리스트 = [3,-20,-3,44]
# for문을 사용해서 리스트의 음수를 출력해라
for i in 리스트:
    if i < 0 :
        print(i)
"""

"""
# 22. for문을 사용해서 3의 배수만을 출력해라
리스트 = [3,100,23,44]
for i in 리스트:
    if i % 3 == 0 :
        print(i)
"""

"""
# 23. 리스트에서 20보다 작은 3의 배수를 출력해라
리스트 = [10,21,12,14,30,18]
for i in 리스트:
    if i < 20 :
        if i % 3 == 0:
            print(i)
"""

"""
# 24. 리스트에서 세 글자 이상의 문자를 화면에 출력하라
리스트 = ["I","study","python","language","!"]
for i in 리스트 :
    if len(i) >= 3 :
        print(i)
"""

"""
# 25. 리스트에서 대문자만 화면에 출력하라
리스트 = ["A","b","c","D"]
for i in 리스트:
    if i.isupper() :
        print(i)
"""

"""
# 26. 리스트에서 소문자만 화면에 출력해라
리스트 = ["A","b","c","D"]
for i in 리스트:
    if i.islower() :
        print(i)
"""

"""
# 27. 이름의 첫 글자를 대문자로 변경해서 출력하라
리스트 = ['dog','cat','parrot']
for i in 리스트:
    i = i.capitalize()
    print(i)
"""

"""
# 28. 파일 이름이 저장된 리스트에서 ㅓ확장자를 제거하고 파일 이름만 화면에 출력하라
리스트 = ['hello.py','ex01.py','intro.hwp']
for i in 리스트:
    print(i.split('.')[0])
"""

"""
# 29. 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력해라
리스트 = ['intra.h','intra.c','define.h','run.py']
for i in 리스트:
    if i.split('.')[1] == "h":
        print(i)
"""

"""
# 30. 파일 이름이 저장된 리스트에서 확장자가 .h나.c인 파일을 화면에 출력해라
리스트 = ['intra.h','intra.c','define.h','run.py']
for i in 리스트:
    if i.split('.')[1] == "h":
        print(i)
    if i.split('.')[1] == "c":
        print(i)
"""

"""
# 31. for문과 range 구문을 사용하여 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라
for i in range(0,100):
    print(i)
"""

"""
# 32. 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 월드컵이 개최되는 연도를 출력해라
for i in range(2002,2051):
    if i % 4 == 2:
        print(i)
"""

"""
# 33. 1부터 30까지의 숫자 중 3의 배수를 출력해라
for i in range(1,31):
    if i % 3 == 0:
        print(i)
"""

"""
# 34. 99부터 0까지 1씩 감소하는 수자들을 한 라인에 하나씩 출력해라
for i in range(1,101):
    print(100 - i)
"""

"""
# 35. for문을 이용해서 아래와 같이 출력해라
# 0.1
# 0.2
# 0.3
# ...
# 0.9
for i in range(0,10):
    print("{0:.1f}".format( i * 0.1 ))
"""

"""
# 36. 구구단 3단을 출력해라
for i in range(1,10):
    print(3,"X",i,"=",i*3)
"""

"""
# 37. 구구단 3단을 출력해라(단 홀수만)
for i in range(1,10):
    if i % 2 == 1:
        print(3,"X",i,"=",i*3)
"""

"""
# 38. 1 ~ 10까지의 숫자에 대해 모두 더한 값을 출력하시오
sum = 0
for i in range(1,11):
    sum += i
print(sum)
"""

"""
# 39. 1 ~ 10까지의 모든 홀수의 숫자에 대해 모두 더한 값을 출력하시오
sum = 0
for i in range(1,11):
    if i % 2 == 1 :
        sum += i
print(sum)
"""

"""
# 40. 1 ~ 10까지의 모든 숫자를 모두 곱한 값을 출력하는 프로그램을 for문을 사용해서 작성하시오
sum = 1
for i in range(1,11):
    sum *= i
print(sum)
"""

"""
# 41. 아래와 같이 리스트의 데이터를 출력해라. 단 for문과 range문을 사용
price_list = [32100,32150,32000,32500]
for i in range(0,4):
    print(price_list[i])
"""

"""
# 42. 아래와 같이 리스트의 데이터를 출력해라. 단 for문과 range문 사용
price_list = [32100,32150,32000,32500]
for i in range(0,4):
    print(i,price_list[i])
"""

"""
# 43. 아래와 같이 리스트의 데이터를 출력해라. 단 for문과 range문을 사용
price_list = [32100,32150,32000,32500]
for i in range(0,4):
    print(3 - i,price_list[i])
"""

"""
# 44. 아래와 같이 리스트의 데이터를 출력해라. 단 for문과 range문을 사용
price_list = [32100,32150,32000,32500]
for i in range(0,3):
    print(100 + i * 10,price_list[i + 1])
"""

"""
# 45. my_list를 아래와 같이 출력해라.
my_list = ["가","나","다","라"]
for i in range(0,2):
    print(my_list[i],end=" ")
print("")
for i in range(1,3):
    print(my_list[i],end=" ")
print("")
for i in range(2,4):
    print(my_list[i],end=" ")
print("")
"""

"""
# 46. 리스트를 아래와 같이 출력해라.
my_list = ["가","나","다","라","마"]
for i in range(0,3):
    print(my_list[i],end=" ")
print("")
for i in range(1,4):
    print(my_list[i],end=" ")
print("")
for i in range(2,5):
    print(my_list[i],end=" ")
print("")
"""

"""
# 47. 리스트를 아래와 같이 출력해라.
my_list = ["가","나","다","라"]
my_list.reverse()
for i in range(0,2):
    print(my_list[i],end=" ")
print("")
for i in range(1,3):
    print(my_list[i],end=" ")
print("")
for i in range(2,4):
    print(my_list[i],end=" ")
print("")
"""

"""
# 48. 리스트에는 네개의 정수가 저장되어 있다. 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.
my_lsit = [100,200,400,800]
for i in range(3):
    print(my_lsit[i + 1] - my_lsit[i])
"""

"""
# 49. 리스트에는 6일 간의 종가 데이터가 저장되어 있따. 종가 데이터의 3일 이동 평균을 계산하고 출력해라.
my_list = [100,200,400,800,1000,1300]
for i in range(4):
    print((my_list[i] + my_list[i + 1] + my_list[i + 2]) / 3)
"""

"""
# 50. 리스트에는 5일간의 저가, 고가 정보가 저장되어 있다. 고가와 저가의 차를 변동폭이라고 정의 할 때 low, high 두개의 리스트를 이용해 변동폭을 volatility 리스트에 저장해라
low_prices = [100,200,400,800,1000]
high_prices = [150,300,430,880,1000]
volatility = []
for i in range(5):
    volatility.append(high_prices[i]-low_prices[i])
"""

"""
# 51. 아래 표에서 하나의 행을 하나의 리스트로. 총 3개의 리스트를 갖는 이차워 리스트 apart를 정의 하라
apart = [[1,2],[1,2],[1,2]]
for i in range(0,3):
    apart[i][0] = 100 * (i + 1) + 1
    apart[i][1] = 100 * (i + 1) + 2
print(apart)
"""

"""
# 52. 아래 표에서 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의 하시오
stock = [[1,2],[1,2],[1,2]]
list = [100,80,200,210,300,330]
for i in range(3):
    stock[i][0] = list[i * 2]
    stock[i][1] = list[i * 2 + 1]
print(stock)
"""

"""
# 53. 아래 표를 stock이름의 딕셔너리로 표현하라. 시가를 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장해라.
stock = {}
list = [100,80,200,210,300,330]
for i in range(3):
    stock[list[i * 2]] = list[i * 2 + 1]
print(stock)
"""

"""
# 54. 아래 표를 stock이름의 딕셔너리로 표현하라. 날짜를 key로 저장하고 나머지 헹의 데이터를 리스트로 저장해서 value로 저장해라.
stock = {}
list2 = ["10/10","10/11"]
list = [80,110,70,90,210,230,190,200]
for i in range(2):
    stock[list2[i]] = list[i * 2 + 1],list[i * 2 + 2],list[i * 2 + 3],list[i * 2 + 4]
print(stock)
"""

"""
# 55. 리스트에 저장된 데이터를 아래와 같이 출력해라.
apart = [[101,102],[201,202],[301,302]]
for i in range(3):
    print(apart[i][0],"호")
    print(apart[i][1],"호")
"""

"""
# 56. 리스트에 저장된 데이터를 아래와 같이 출력해라.
apart = [[101,102],[201,202],[301,302]]
for i in range(3):
    print(apart[2 - i][0],"호")
    print(apart[2 - i][1],"호")
"""

"""
# 57. 리스트에 저장된 데이터를 아래와 같이 출력해라.
apart = [[101,102],[201,202],[301,302]]
for i in range(3):
    print(apart[2 - i][1],"호")
    print(apart[2 - i][0],"호")
"""

"""
# 58. 리스트에 저장된 데이터를 아래와 같이 출력해라.
apart = [[101,102],[201,202],[301,302]]
for i in range(3):
    print(apart[i][0],"호")
    print("-----")
    print(apart[i][1],"호")
    print("-----")
"""

"""
# 59. 리스트에 저장된 데이터를 아래와 같이 출력해라.
apart = [[101,102],[201,202],[301,302]]
for i in range(3):
    print(apart[i][0],"호")
    print(apart[i][1],"호")
    print("-----")
"""

"""
# 60. 리스트에 저장된 데이터를 아래와 같이 출력해라.
apart = [[101,102],[201,202],[301,302]]
for i in range(3):
    print(apart[i][0],"호")
    print(apart[i][1],"호")
print("-----")
"""

"""
# 61. data에는 매수한 종목들의 OHLC 가격 정보가 바인딩 되어 있다.
data = [[2000,3050,2050,1980],[7500,2050,2050,1980],[15450,15050,15550,14900]]
# 수수료를 0.014%로 가정할 때, 각 가격에 수수료를 포함한 가격을 한 라인에 하나씩 출력하라.
for i in range(3):
    for a in range(4):
        print(data[i][a] + data[i][a] * 0.014)
"""

"""
# 62. 61번의 출력 결과에 행 단위로 "----" 구분자를 추가해라
data = [[2000,3050,2050,1980],[7500,2050,2050,1980],[15450,15050,15550,14900]]
for i in range(3):
    for a in range(4):
        print(data[i][a] + data[i][a] * 0.014)
    print("----")
"""

"""
# 63. 61번의 문제의 결과값을 result이름의 리스트에 1차원 배열로 저장해라.
data = [[2000,3050,2050,1980],[7500,2050,2050,1980],[15450,15050,15550,14900]]
result = []
for i in range(3):
    for a in range(4):
        result.append(data[i][a] + data[i][a] * 0.014)
print(result)
"""

"""
# 64. 61번의 문제의 결과값을 result이름의 리스트에 2차원 배열로 저장해라.
data = [[2000,3050,2050,1980],[7500,2050,2050,1980],[15450,15050,15550,14900]]
result = [[],[],[]]
for i in range(3):
    for a in range(4):
        result[i].append(data[i][a] + data[i][a] * 0.014)
print(result)
"""

"""
# 65. ohlc 리스트에는 시가(open), 고가(high), 저가(low), 종가(close)가 날짜 별로 저장되 있다. 화면에 종가 데이터를 출력해라.
ohlc = [["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for i in range(3):
    print(ohlc[i + 1][3])
"""

"""
# 66. ohlc리스트에는 시가, 고가, 저가, 종가가 날짜 별로 저장되어 있다. 종가가 150원보다 큰 경우에만 종가를 출력해라.
ohlc = [["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for i in range(3):
    if ohlc[i + 1][3] > 150 :
        print(ohlc[i + 1][3])
"""

"""
# 67. ohlc리스트에는 시가, 고가, 저가, 종가가 날짜별로 저장되어 있다. 종가가 시가보다 크거나 같은 경우에만 종가를 출력해라
ohlc = [["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for i in range(3):
    if ohlc[i + 1][3] >= ohlc[i + 1][0]:
        print(ohlc[i + 1][3])
"""

"""
# 68. ohlc리스트에는 시가, 고가, 저가, 종가가 날짜별로 저장되어 있다. 고가와 저가의 차이를 변동폭으로 정의 할 때 변동폭을 volatility이름의 리스트에 저장해라.
ohlc = [["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
volatility = []
for i in range(3):
    volatility.append(ohlc[i + 1][1] - ohlc[i + 1][2])
print(volatility)
"""

"""
# 69. 리스트에는 3일간의 ohlc데이터가 저장되어 있다. 종가가 시가보다 높은 날의 변동성 (고가 - 저가)을 화면에 출력해라
ohlc = [["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for i in range(3):
    if ohlc[i + 1][3] > ohlc[i + 1][0]:
        print(ohlc[i + 1][3] - ohlc[i + 1][0])
"""

"""
# 70. 리스트에는 3일 간의 ohlc 데이터가 저장되어 있다. 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산해라.
ohlc = [["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for i in range(3):
    print(i + 1 , "일차 수익 ", ohlc[i + 1][3] - ohlc[i + 1][0],"원")
"""