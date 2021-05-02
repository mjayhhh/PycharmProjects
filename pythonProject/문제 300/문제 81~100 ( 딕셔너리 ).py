# 81. 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, star expression을 사용하여 우측 8개의 값을
# valid_score 변수에 바인딩하여라라
scores = [8.8,8.9,8.7,9.2,9.3,9.7,9.9,9.5,7.8,9.4]
a,b,*valid_score = scores
print(valid_score)

# 82. 다음과 같이 10개의 값이 저장된 scores리스트가 있을 떄, star expression을 사용하여 좌측 8개의 값을
# valid_score 변수에 바인딩하여라
scores = [8.8,8.9,8.7,9.2,9.3,9.7,9.9,9.5,7.8,9.4]
*valid_score,a,b = scores
print(valid_score)

# 83. 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, star expression을 사용하여 가운데 8개의 값을
# valid_score 변수에 바인딩하여라
scores = [8.8,8.9,8.7,9.2,9.3,9.7,9.9,9.5,7.8,9.4]
a,*valid_score,b = scores
print(valid_score)

# 84. temp 이름의 비어있는 딕셔너리를 만들어라
temp = {}

# 85. 다음 아이스크림 이름과 희망 가격을 딕셔너리롤 구성해라.
ice_cream = {'메로나':1000,'폴라포':1200,'빵빠레':1800}
print(ice_cream)

# 86. 85번의 딕셔너리에 아래 아이스크림 가격정보를 추가해라.
ice_cream["죠스바"] = 1200
ice_cream["월드콘"] = 1500
print(ice_cream)

# 87. 다음 딕셔너리를 사용하여 메로나 가격을 출력해라.
ice_cream = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
print(ice_cream['메로나'])

# 88. 다음 딕셔너리의 메로나의 가격을 1300으로 수정해라
ice_cream['메로나'] = 1300
print(ice_cream)

# 89. 다음 딕셔너리에서 메로나를 삭제해라.
del(ice_cream['메로나'])
print(ice_cream)

# 90. 다음 코드에서 에러가 발생한 원인을 설명해라
# ice_cream = {'폴라포':1200,'빵빠레':1800,'월드콘':1500,'메로나':1000}
# ice_cream['누가바']
# 딕셔너리는 키와 그 키의 값이 있어야하는데 키값을 입력하지 않아서

# 91. 아래 표에서 아이스크림을 키값으로, 리스트를 딕셔너리의 값으로 저장해라. 딕셔너리의 이름은
# inventory라고 한다
inventory = {'메로나': [300,20] ,'비비빅':[400,3],'죠스바':[250,100]}

# 92. inventory 딕셔너리에서 메로나의 가격을 화면에 출력해라
print(inventory['메로나'][0])

# 93. inventory 딕셔너리에서 메로나의 재고를 화면에 출력해라
print(inventory['메로나'][1])

# 94. 딕셔너리에 아래 데이터를 추가해라
inventory['월드콘'] = [500,7]
print(inventory)

# 95. 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성해라.
ice_cream = {'탱크보이':1200,'폴라포':1200,'빵빠레':1800,'월드콘':1500,'메로나':1000}
key = []
for i in ice_cream:
    key.append(i)
print(key)

# 96. 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성해라.
ice_cream = {'탱크보이':1200,'폴라포':1200,'빵빠레':1800,'월드콘':1500,'메로나':1000}
value = []
for i in ice_cream:
    value.append(ice_cream[i])
print(value)

# 97. ice_cream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력해라
sum = 0
for i in value:
    sum += i
print(sum)

# 98. 아래의 new_product 딕셔너리를 다음 ice_cream 딕셔너리에 추가해라
ice_cream = {'탱크보이':1200,'폴라포':1200,'빵빠레':1800,'월드콘':1500,'메로나':1000}
new_product = {'팥빙수':2700,'아맛나':1000}
ice_cream.update(new_product)
print(ice_cream)

# 99. 아래 두 개의 튜플을 하나의 딕셔너리로 변환해라. keys를 키로, vals를 값으로 result이름의 딕셔너리로 저장한다
keys = ("apple","pear","peach")
vals = (300,250,400)
result = {}
for i in range(3):
    result[keys[i]] = vals[i]
print(result)

# 100. date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라
date = ['09/05','09/06','09/07','09/08','09/09']
close_price = [10500,10300,10100,10800,11000]
close_table = {}
for i in range(3):
    close_table[date[i]] = close_price[i]
print(close_table)