
#51. 리스트 생성
movie_rank = [ "닥터 스트레인지","스플릿","럭키"]

#52. 리스트 추가  append
movie_rank.append( "배트맨")
print(movie_rank)

#53. 리스트 삽입 insert
movie_rank.insert( 1 , "슈퍼맨" )
print(movie_rank)

#54. 리스트 삭제 del
del movie_rank[3]
print("럭키[3] 삭제 후 ",movie_rank)

#55. 리스트 삭제 del
del movie_rank[2] # 세번째 값 삭제  : 3-> 2
del movie_rank[2] # 세번째 값 삭제
print("2번 삭제후 ",movie_rank)

#56. 리스트 연결
lang1 = ["C","C++","JAVA"]
lang2 = ["Python","Go","C#"]
langs = lang1 + lang2
print(" 두 리스트 연결 ", langs)

#57. 리스트의 최댓값, 최솟값 함수 사용   # max(리스트) # min(리스트)
nums = [1,2,3,4,5,6,7]
print("최댓값max ", max(nums) )
print("최솟값min ", min(nums) )

#58. 리스트의 함수 # sum
nums = [ 1 , 2 ,3 ,4 , 5]
print("합계sum " , sum(nums))

#59. 리스트의 개수 # len
cook = ["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","쏘세지","라면","팥빙수","김치전"]
print( len(cook) )

#60. 리스트의 평균 : 합계 / 개수  # sum / len
nums=[1,2,3,4,5]
평균 = sum(nums) / len( nums )
print("평균 sum/len : ", 평균 )

#61. 리스트내 특정 부분만 출력 [ 슬라이싱 : ]
price=[ '20180728' , 100 , 130 , 140 , 150 , 160 , 170]
print( price[ 1: ] ) # 2번째 값부터 생략[끝]까지

#62. 리스트내 홀수만 출력
nums = [ 1,2,3,4,5,6,7,8,9,10]
print("리스트내 홀수 : ", nums[ : :2 ])
                        #  : : 2
                        # 0부터 2단위 => 인덱스 짝수만 출력
#63. 리스트내 짝수만 출력
print("리스트내 짝수 : " , nums[ 1 : : 2 ])
                        # 1 : : 2
                        # 1부터 2단위 => 인덱스 짝수만 출력
#64. 리스트 역순
nums=[1,2,3,4,5]
print("리스트의 역순 : ", nums[ : : -1 ])
                        # : : -1
#65. 리스트 출력
interest=["삼성전자","LG전자","Naver"]
print( interest[0] , interest[2] )

interest = ["삼성전자","LG전자","Naver","SK하이닉스","미래에셋대우"]
print(" 리스트내 값을 공백으로 합치기 : ", " ".join(interest) )

#67. join 함수 : / 합치기
print(" 리스트내 값을 / 로 합치기 : ", "/".join(interest))

#68. join 함수 : 줄바꿈 \n 합치기   [ 엔터 위 => 원화 \
print(" 리스트내 값을 줄바꿈 으로 합치기 " , "\n".join(interest))

#69. split 함수 : 분리 함수
string = "삼성전자/LG전자/Naver"
print(" 문자내 기호 기준으로 분리 : ", string.split("/"))

#70.
date =[2,4,3,1,5,10,9]
date.sort() # 오름차순으로 정렬하기
print(" 리스트내 오름차순으로 정렬 : " , date)

