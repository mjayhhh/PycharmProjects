# 71. my_variable 이름의 비어있는 튜플을 만들어라
my_variable = ()

# 72. 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank이름의 튜플에 저장해라.
movie_rank = ("닥터 스트레인지","스플릿","럭키")

# 73. 숫자 1이 저장된 튜플을 생성해라
Tuple = (1)

# 74. 다음 코드를 실행해보고 오류가 발생하는 원인을 설명해라
# t = (1,2,3)
# t[0] = 'a'
# 튜플을 값을 바꿀수가 없는데 바꾸려고 해서 오류가 난거다

# 75. 아래와 같이 t에는 1,2,3,4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
t = 1,2,3,4
# 튜플

# 76. 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A','b','c')튜플을 가리키도록 수정해라.
t = ('a','b','c')

# 77. 다음 튜플을 리스트로 변환해라
interest = ('삼성전자','LG전자','Sk Hynix')
interest = list(interest)
print(interest)

# 78. 다음 리스트를 튜플로 변환해라.
interest = ['삼성전자','LG전자','Sk Hynix']
interest = ('삼성전자','LG전자','Sk Hynix')

# 79. 다음 코드의 실행 결과를 예상해라.
temp = ('apple','banana','cake')
a,b,c = temp
print(a,b,c)
# apple banana cake

# 80. 1부터 99까지의 정수중 짝수만 저장된 튜플을 생성해라
Tuple = []
for i in range(1,100):
    if i % 2 == 0:
        Tuple.append(i)
Tuple2 = tuple(Tuple)
print(Tuple2)