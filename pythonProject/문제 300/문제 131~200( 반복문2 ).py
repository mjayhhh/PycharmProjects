# 131. for문의 실행 결과를 예측해라.
과일 = ["사과","귤","수박"]
for 변수 in 과일:
    print("변수")
# 사과
# 귤
# 수박

# 132. for문의 실행결과를 예측해라.
과일 = ["사과","귤","수박"]
for 변수 in 과일:
    print("#####")
# #####
# #####
# #####

# 133. 다음 for문과 동일한 기능을 수행하는 코드를 작성하세요.
for 변수 in ["A","B","C"]:
    print(변수)

print('A')
print("B")
print("C")

# 135. for문을 풀어서 동일한 동작을 하는 코드를 작성해라.
for 변수 in ["A","B","C"]:
    b = 변수.lower()
    print("변환 :", b)

print("a")
print("b")
print("c")

# 136. 다음 코드를 for문으로 작성해라.
변수 = 10
print(변수)
변수 = 20
print(변수)
변수 = 30
print(변수)
#  ㅣ
for i in [10,20,30]:
    변수 = i
    print(변수)

# 137. 다음 코드를 for문으로 작성해라.
print(10)
print(20)
print(30)
#  ㅣ
for i in [10,20,30]:
    print(i)

# 138. 다음 코드를 for문으로 작성해라.
print(10)
print("-------")
print(20)
print("-------")
print(30)
print("-------")
#    ㅣ
for a in [10,20,30]:
    print(a)
    print("-------")

# 139. 다음 코드를 for문으로 작성해라.
print("++++")
print(10)
print(20)
print(30)
#   ㅣ
print("++++")
for i in range(3):
    print(10 + 10 * i)

# 140. 다음 코드를 for문으로 작성해라.
print("-------")
print("-------")
print("-------")
print("-------")
#     ㅣ
for i in range(4):
    print("-------")

# 141. 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력해라. 단 부가
# 세는 10원으로 가정한다.
리스트 = [100,200,300]
for a in range(1,4):
    print(100 * a + 10)

# 142. for문을 사용해서 리스트에 저장된 값을 다음과 같이 출력해라.
리스트 = ["김밥","라면","튀김"]
for i in 리스트:
    print("오늘의 메뉴 :", i)

# 143. 리스트에 주식 종목이름이 저장되어 있따.
리스트 = ["SK하이닉스","삼성전자","LG전자"]
for i in 리스트:
    print(len(i))

# 144. 리스트에는 동물이름이 문자열로 저장되어 있다.
리스트 = ['dog','cat','parrot']
for i in 리스트:
    print(i,len(i))

# 145. 리스트에 동물 이름이 저장되어 있다. for문을 이용해 동물 이름의 첫 글자만 출력해라.
리스트 = ['dog','cat','parrot']
for i in 리스트:
    print(i[0])

# 146. 리스트에는 세 개의 숫자가 바인딩 되어 있다. for문을 사용해 3단을 3개 만들어라
리스트 = [1,2,3]
for a in 리스트:
    print("3 x",a)

# 148. 리스트에는 네 개의 숫자가 바인딩 되어 있다. for문을 사용해 3단을 3개 만들어라
리스트 = [1,2,3]
for a in 리스트:
    print("3 x",a,"=",a * 3)

# 148. 리스트에는 네 개의 숫자가 바인딩 되어 있다. for문을 사용해 가를 뺀 나머지를 출력하시오
리스트 = ["가","나","다","라"]
리스트.pop(0)
for a in 리스트:
    print(a)

# 149. 리스트에는 네 개의 문자열이 바인딩 되어 있다. for문을 이용해 다음과 같이 출력해라.
리스트 = ["가","나","다","라"]
for a in 리스트:
    if a == "가" or "다":
        print(a)
    pass

# 150. 리트스에는 네 개의 문자열이 바인딩 되어 있다. for문을 이용해서 다음과 같이 출력해라.
리스트 = ["가","나","다","라"]
리스트 = sorted(리스트, reverse=True)
for a in 리스트:
    print(a)

# 151. 리스트에는 네 개의 정수가 저장되어 있다.
리스트 = [3,-20,-3,44]
# for 문을 이용해서 음수를 출력해라.
for i in 리스트 :
    if i < 0 :
        print(i)

# 152. for문을 이요해서 3의 배수만 출력해라
리스트 = [3,100,23,44]
for i in 리스트:
    if i % 3 == 0 :
        print(i)

# 153. 리스트에서 20보다 작은 3의 배수를 출력해라
리스트 = [12,21,12,14,30,18]
for i in 리스트 :
    if i < 20 and i % 3 == 0 :
        print(i)

# 154. 리스트에서 세 글자 이상의 문자를 화면 출력해라
리스트 = ["I","study","python","language","!"]
for i in 리스트 :
    if len(i) >= 3 :
        print(i)

# 155. 리스트에서 대문자만 화면에 출력해라
리스트 = ["A","b","c","D"]
for i in 리스트 :
    if i.isupper() :
        print(i)

# 156. 리스트에서 소문자만 화면에 출력해라
리스트 = ["A","b","c","D"]
for i in 리스트 :
    if i.islower() :
        print(i)

# 157. 이름의 첫 글자를 대문자로 변경해서 출력해라
리스트 = ['dog','cat','parrot']
for i in 리스트 :
    print(i[0].upper(), end='')
    for a in range(len(i) - 1):
        print(i[a + 1], end='')
    print()

# 158. 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력해라.
리스트 = ["hello.py","ex01.py","intro.hwp"]
for i in 리스트 :
    i = i.split('.')
    print(i[0])

# 159. 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력해라.
리스트 = ["intra.h",'intra.c','define.h','run.py']
for i in 리스트 :
    i = i.split('.')
    if i[1] == "h":
        print(i[0] + "." + i[1])

# 160. 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력해라.
리스트 = ["intra.h",'intra.c','define.h','run.py']
for i in 리스트 :
    i = i.split('.')
    if i[1] == "h" or i[1] == "c":
        print(i[0] + "." + i[1])

# 161. for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성해라.
for i in range(100):
    print(i)

# 162. 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력해라.
for i in range(2002,2051,4):
    print(i)

# 163. 1부터 30까지의 숫자 중 3의 배수를 출력해라.
for i in range(3,31,3):
    print(i)

# 164. 99부터 0까지 1씩 감소하는 수자들을 한 라인에 하나씩 출력해라.
for i in range(1,101):
    print(100 - i)

# 165. for문을 사용해서 아래와 같이 출력해라.
# 0.1
# 0.2
# ...
# 0.9
for i in range(1,10):
    print(round(i * 0.1,1))

# 166. 구구단 3단을 출력해라.
for i in range(1,10):
    print("3 X", i, "=", 3 * i)

# 167. 구구단 3단을 출력해라. 단 홀수 번째만 출력한다.
for i in range(1,10,2):
    print("3 X", i, "=", 3 * i)

# 168. 1~10까지의 숫자의 대해 모두 더한 값을 출력하는 프로그램 for문을 사용해서 작성해라.
sum = 0
for i in range(1,11):
    sum += i
print(sum)


# 169. 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for문을 사용해서 작성해라.
sum = 0
for i in range(1,10, 2):
    sum += i
print(sum)

# 170. 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for문을 사용해서 작성해라.
sum = 0
for i in range(1,10):
    if sum == 0 :
        sum += i
    sum *= i
print(sum)

# 171. 아래와 같이 리스트의 데이터를 출력해라. 단 for문과 range문을 사용해라
price_list = [32100,32150,32000,32500]
for i in price_list:
    print(i)

# 172. 아래와 같이 리스트의 데이터를 출력해라. 단 for문과 range문을 사용해라
price_list = [32100,32150,32000,32500]
for i in price_list:
    for a in range(4):
        print(a, price_list[a])
    break

# 173. 아래와 같이 리스트의 데이터를 출력해라. 단 for문과 range문을 사용해라
price_list = [32100,32150,32000,32500]
for i in price_list:
    for a in range(4):
        print(3 - a, price_list[a])
    break

# 174. 아래와 같이 리스트의 데이터를 출력해라. 단 for문과 range문을 사용해라
price_list = [32100,32150,32000,32500]
for i in price_list:
    for a in range(3):
        print(100 + a * 10, price_list[a + 1])
    break

# 175. my_list를 아래와 같이 출력해라
my_list = ["가","나","다","라"]
for i in range(0,3):
    print(my_list[i], my_list[i + 1])

# 176. 리스트를 아래와 같이 출력해라.
my_list = ["가","나","다","라","마"]
for i in range(0,3):
    print(my_list[i], my_list[i + 1], my_list[i + 2])

# 177. 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력해라.
my_list = ["가","나","다","라"]
for i in range(0,3):
    print(my_list[3 - i], my_list[2 - i])

# 178. 리스트에는 네 개의 정수가 저장되어 있따. 가가의 데이터에 대해서 자신과 우측값과의 기본값을 화면에 출력해라.
my_list= [100,200,400,800]
for i in range(0,3):
    print(my_list[i + 1] - my_list[i])

# 179. 리스트에는 6일 간의 종각 데이터가 저장되어 있다. 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력해라.
my_list = [100,200,400,800,1000,1300]
for i in range(0,4):
    print((my_list[i] + my_list[i + 1] + my_list[i + 2]) // 3)

# 180. 리스트에 5일간의 조가, 고가 정보가 저장되어 있따. 고가와 저가의 차를 변동폭이라고 정의 할떄, low, high 두 개의
# 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장해라.
low_prices = [100,200,400,800,1000]
high_prices = [150,300,430,880,1000]
volatility = []
for i in range(5):
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)

# 181. 아래 표에서 하나의 행을 하나의 리스트로, 총 3개의 리스트를 갖는 이차원 리스트 apart를 정의해라.
apart = []
for i in range(1,4):
    apart.append([100 * i + 1, 100 * i + 2])
print(apart)

# 182. 아래 표에서 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의해라.
stock = [[100,200,300],[80,210,330]]

# 183. 아래 표를 stock 이름의 딕셔너리로 표현하라. 시가를 key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서
# value로 저장한다. 종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.
stock = {"key": [100, 200, 300], 'value': [80, 210, 330]}

# 184. 아래 표를 stock 이라는 이름의 딕셔너리로 표현해라. 날짜를 eky로 저장하고 나머지 같은 행의 데이터를 리스트로
# 저장해서 value로 저장한다. 첫 열이 날짜이다
stock = {"10/10":[80,100,70,90],"10/11":[210,230,190,200]}

# 185. 리스트에 저장된 데이터를 아래와 같이 출력해라.
apart = [[101,102],[201,202],[301,302]]
for i in range(3):
    for a in range(2):
        print(apart[i][a] ,"호")

# 186. 리스트에 저장된 데이터를 아래와 같이 출력해라.
apart = [[101,102],[201,202],[301,302]]
for i in range(3):
    for a in range(2):
        print(apart[2 - i][a] ,"호")

# 187. 리스트에 저장된 데이터를 아래와 같이 출력해라.
apart = [[101,102],[201,202],[301,302]]
for i in range(3):
    for a in range(2):
        print(apart[2 - i][1 - a] ,"호")

# 188. 리스트에 저장된 데이터를 아래와 같이 출력해라.
apart = [[101,102],[201,202],[301,302]]
for i in range(3):
    for a in range(2):
        print(apart[i][a] ,"호")
        print('-------')

# 189. 리스트에 저장된 데이터를 아래와 같이 출력해라.
apart = [[101,102],[201,202],[301,302]]
for i in range(3):
    for a in range(2):
        print(apart[i][a] ,"호")
    print('-------')

# 190. 리스트에 저장된 데이터를 아래와 같이 출력해라.
apart = [[101,102],[201,202],[301,302]]
for i in range(3):
    for a in range(2):
        print(apart[i][a] ,"호")
print('-------')

# 191. data에는 매수한 종목들의 OHLC (oepn/high/low/close) 가격 정보가 바인딩 되어 있다
data = [[2000, 3050, 2050, 1980], [7500, 2050, 2050, 1980], [15450, 15050, 15550, 14900]]
# 수수료를 0.014%로 가정할 때, 각 수수료를 포함한 가격을 한라인에 하나씩 출력해라.
for i in range(3):
    for a in range(4):
        print(data[i][a] + data[i][a] * 0.014)

# 192. 191번의 출력 결과에 행단위 "----" 구분자를 추가해라.
data = [[2000, 3050, 2050, 1980], [7500, 2050, 2050, 1980], [15450, 15050, 15550, 14900]]
for i in range(3):
    for a in range(4):
        print(data[i][a] + data[i][a] * 0.014)
    print("----")

# 193. 192번 문제의 결괏값을 result이름의 리스트에 1차원 배열로 저장해라.
result = []
data = [[2000, 3050, 2050, 1980], [7500, 2050, 2050, 1980], [15450, 15050, 15550, 14900]]
for i in range(3):
    for a in range(4):
        result.append(data[i][a] + data[i][a] * 0.014)

# 194. 방금 저장했던 result 이름의 1차원 리스트를 2차원 배열로 저장해라.
result2 = []
for i in range(0,12,4):
    result2.append([result[i], result[i + 1], result[i + 2], result[i + 3]])
print(result2)

# 195. ohlc 리스트에는 시가(open), 고가(high), 저가(low), 종가(close)가 날짜별로 저장되어 있다. 화면에 종가데이터를 출
# 력해라.
ohlc = [["open", "high", "low", "close"], [100, 110, 70, 100], [200, 210, 180, 190], [300, 310, 300, 310]]
for i in range(1, 4):
    print(ohlc[i][3])

# 196. ohlc 리스트에는 시가(open), 고가(high), 저가(low), 종가(close)가 날짜별로 저장되어 있다. 화면에 150원보다 큰 종가데이터를 출
# 력해라.
ohlc = [["open", "high", "low", "close"], [100, 110, 70, 100], [200, 210, 180, 190], [300, 310, 300, 310]]
for i in range(1, 4):
    if ohlc[i][3] > 150 :
        print(ohlc[i][3])

# 197. ohlc 리스트에는 시가(open), 고가(high), 저가(low), 종가(close)가 날짜별로 저장되어 있다. 화면에 시가보다 크거나 같은 종가데이터를 출
# 력해라.
ohlc = [["open", "high", "low", "close"], [100, 110, 70, 100], [200, 210, 180, 190], [300, 310, 300, 310]]
for i in range(1, 4):
    if ohlc[i][3] >= ohlc[i][0] :
        print(ohlc[i][3])

# 198. ohlc 리스트에는 시가(open), 고가(high), 저가(low), 종가(close)가 날짜별로 저장되어 있다. 고가와 저가의 차이를 변동폭으로 정의할
# 때 변동폭을 volatility 이름의 리스트에 저장해라.
ohlc = [["open", "high", "low", "close"], [100, 110, 70, 100], [200, 210, 180, 190], [300, 310, 300, 310]]
volatility = []
for i in range(1, 4):
    volatility.append( ohlc[i][1] - ohlc[i][2] )
print(volatility)

# 199. ohlc 리스트에는 시가(open), 고가(high), 저가(low), 종가(close)가 날짜별로 저장되어 있다. 종가가 시가보다 높은 날의 변동성 ( 고가 - 저가 )을 화면에 출력
# 해라.
ohlc = [["open", "high", "low", "close"], [100, 110, 70, 100], [200, 210, 180, 190], [300, 310, 300, 310]]
for i in range(1, 4):
    if ohlc[i][3] > ohlc[i][0] :
        print(ohlc[i][1] - ohlc[i][2])

# 200. ohlc 리스트에는 시가(open), 고가(high), 저가(low), 종가(close)가 날짜별로 저장되어 있다. 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산해라.
ohlc = [["open", "high", "low", "close"], [100, 110, 70, 100], [200, 210, 180, 190], [300, 310, 300, 310]]
sum = 0
for i in range(1, 4):
    sum += ohlc[i][3] - ohlc[i][0]
print(sum)

# 논리 : 맞는지 틀린지 판단
# 연산자 :
    # 산술 연산자 : + : 더하기, - : 빼기, / : 나누기, // : 나누기(몫), % : 나누기(나머지)
    # 비교 연산자 : > 초과, < : 미만, >= 이상, <= : 이하, == : 같다, != : 같지않다
    # 논리 연산자 : and[ 이면서 ], or[ 이거나 ], ![ 부정 ]
    # 대입 연산자 : +=, -=, /=, *=, //=, %= : =앞에 있는 걸로 계산을 한후 대입

# if : 논리문
    # if 논리 :
        # 논리가 True이면 실행할 코드
    # elif 논리 :
        # 첫 번째 논리가 False이거 두번째 논리가 True이면 실행할 코드
    # else :
        # 첫 번째와 두 번째 논리가 False이면 실행할 코드
    # 논리 안에 논리가 들어갈수 있음
    # if 논리 :
        # if 논리 :
            # 두개다 참이면 실행할 코드
