# 51. 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요
# (순위 정보는 저장하지 않습니다)
movie_rank = []
movie_rank.append("닥터 스트레인지")
movie_rank.append("스플릿")
movie_rank.append("럭키")
print(movie_rank)

# 52. 51의 movie_rank 리스트에 "배트맨"을 추가해라.
movie_rank.append("배트맨")
print(movie_rank)

# 53. movie_rank 리스트에는 아래와 같이 네개의 영화 제목이 바인딩 되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿"
# 사이에 추가해라
movie_rank = ["닥터 스트레인지","스플릿","럭키","배트맨"]
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)

# 54. movie_rank 리스트에서 "럭키"를 삭제해라
movie_rank.pop(3)
print(movie_rank)

# 55. movie_rank 리스트에서 "스플릿"과 "배트맨"을 삭제해라
movie_rank.pop(3)
movie_rank.pop(2)
print(movie_rank)

# 56. lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라
lang1 = ["C",'C++',"Java"]
lang2 = ["Python","Go","C#"]
langs = lang1 + lang2
print(langs)

# 57. 다음 리스트에서 최댓값과 최솟값을 출력해라. ( 힌트 : min(), max() 함수 사용 )
nums = [1,2,3,4,5,6,7]
print(max(nums))
print(min(nums))

# 58. 다음 리스트의 합을 출력해라.
nums = [1,2,3,4,5]
sum= 0
for i in nums :
    sum += i
print(sum)

# 59. 다음 리스트에 저장된 데이터의 개수를 화면에 구하여라
cook = ["피자","김밥",'만두','양념치킨','족발','피자','김치만두','쫄면','쏘세지','라면','팥빙수','김치전']
print(len(cook))

# 60. 다음 리스트의 평균을 출력해라
nums = [1,2,3,4,5]
sum = 0
for i in nums:
    sum += i
print(sum / len(nums))

# 61. price 변수에는 날짜와 종가 정보가 저장되어 있다. 날짜 정보를 제외하고 가격정보만을 출력해라. ( 힌트 : 슬라이싱 )
price = ['20180728',100,130,140,150,160,170]
print(price[1:])

# 62. 슬라이싱을 사용해서 홀수만 출력해라
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[0:10:2])

# 63. 슬라이싱을 사용해서 짝수만 출력해라
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[1:10:2])

# 64. 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력해라
nums = [1,2,3,4,5]
print(nums[5::-1])

# 65. interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자','LG전자','Naver']
print(interest[0],interest[2])

# 66. interest 리스트에는 아래의 데이터가 바인딩 되어 있다.
interest = ['삼성전자',"LG전자","Naver","SK하이닉스","미래에셋대우"]
for i in interest:
    print(i, end=' ')
print()

# 67. interest 리스트에는 아래의 데이터가 바인딩되어 있다
interest = ['삼성전자',"LG전자","Naver","SK하이닉스","미래에셋대우"]
for i in interest:
    print(i, end='/')
print()

# 68. interest 리스트에는 아래의 데이터가 바인딩 되어 있다
interest = ['삼성전자',"LG전자","Naver","SK하이닉스","미래에셋대우"]
for i in interest:
    print(i)

# 69. 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
string = "삼성전자/LG전자/Naver"
# interest 이름의 리스트로 분리해서 저장해라
interest = string.split('/')
print(interest)

# 70. 리스트에 있는 값을 오름차순으로 정렬하세요
data = [2,4,3,1,5,10,9]
data = sorted(data)
print(data)