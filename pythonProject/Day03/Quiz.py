"""
1. 점수를 입력받아 점수가 80점 이상이면 합격 아니면 불합격 출력
score = int(input("점수 : "))
if score >= 80:
    print("합격입니다")
else :
    print("불합격입니다")
"""

"""
2. 입력받은 점수가 90점 이상 : 최우수 / 80점 이상 : 우수 / 70점 이상 : 보통 / 나머지 : 미달
score = int(input("점수 : "))
if score >= 90:
    print("최우수")
elif score >= 80:
    print("우수")
elif score >= 70:
    print("보통")
else :
    print("미달")
"""

"""
3. 3개의 수를 입력받아 가장 큰 수를 출력
num = []
for i in range(3):
    num.append(int(input("수 : ")))
num.sort()
print(num[2])
"""

"""
4. 가위바위보 게임 만들기(가위 : 0, 바위 : 1, 보 : 2)(4를 누르면 종료)
import random
score1 = 0 # 플레이어 점수 값
score2 = 0 # 컴퓨터 점수 값
while True:
    p1 = int(input("가위바위보(가위 : 0, 바위 : 1, 보 : 2, 종료 : 4)"))
    p2 = random.randint(0,2) # 0~2까지의 랜덤 수 
    if p1 == 4: # 4를 입력하면 종료
        break
    elif p1 == p2 : # 둘이 같으면 비김
        print("비겼다")
    elif p1 == 0: # 만약 가위라면
        p1 = 3 # 보를 이길수 잇게 만들기
        if p1 - 1 == p2 :
            print("이겼다")
            score1 += 1 # 플레이어 점수
        else :
            print("졌다") 
            score2 += 1 # 컴퓨터 점수
    elif p1 - 1 == p2: # 1보다 작은수 = 이길수 있는 거
        print("이겼다")
        score1 += 1 # 플레이어 점수 +1
    else :
        print("졌다")
        score2 += 1 # 컴퓨터 점수 +1
if score1 == score2: # 플레이어 점수가 더 높으면
    print("비겼다")
elif score1 > score2: # 컴퓨터 점수가 더 높으면
    print("승리")
else:
    print("패배")
"""

"""
2-1. 2단 만들기
for i in range(1,10):
    print("2 X", i  ,"=", i * 2)
  
2-2. 입력한 구구단 출력
num = int(input("출력할 단 : "))
for i in range(1,10):
    print(num, "X", i, "=", num * i)
    
2-3. 모든 구구단 출력
for i in range(1,10):
    print("=====" ,i, "단 =====")
    for a in range(1,10):
        print(i,"X",a,"=", a * i)
"""

"""
[순서도]
for 단 : 2 for 문 : 1, 2, 3, 4, 5, 6, 7, 8, 9
for 단 : 3 for 문 : 1, 2, 3, 4, 5, 6, 7, 8, 9
for 단 : 4 for 문 : 1, 2, 3, 4, 5, 6, 7, 8, 9
===================== 생략
for 단 : 9 for 문 : 1, 2, 3, 4, 5, 6, 7, 8, 9
"""

"""
3. 별 모양 출력
"""

