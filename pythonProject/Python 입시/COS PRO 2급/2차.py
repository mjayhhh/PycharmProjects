# 문제 1번
max_product_number = 10  # 10이라는 값을 저장하는 max_product_number 변수 만들기

def func_a(gloves):   # func_a 함수 만들기
    counter = [0 for _ in range(max_product_number + 1)]  # 0으로 max_product_number의 값이 1을 더한 값만큼 리스트를 만들고 채우기
    for x in gloves:  # gloves의 값을 차례로 x에 넣으면서 반복
        counter[x] += 1  # x번째의 값에 1을 더하기
    return counter  # return의 값을 반환하기

def solution(left_gloves, right_gloves):  # solution 함수 만들기
    left_counter = func_a(left_gloves)  # left_gloves의 값을 넣으면서 func_a 함수 실행하기
    right_counter = func_a(right_gloves)  # right_gloves의 값을 넣으면서 func_a 함수 실행하기

    total = 0  # 합계를 저장할 변수 만들기
    for i in range(1, max_product_number + 1): # 1부터 max_product_number에 값에 1을 더한 값 까지 1씩 더하면서 반복하기
        total += min(left_counter[i], right_counter[i])  # total에 left_counter의 i번째 값과 right_counter[i]의 i번째 값 중 작은걸 더하기
    return total  # total의 값을 반환하기

left_gloves = [2, 1, 2, 2, 4]  # 숫자를 저장하는 left_gloves 리스트 만들기
right_gloves = [1, 2, 2, 4, 4, 7]  # 숫자를 저장하는 right_gloves 리스트 만들기
ret = solution(left_gloves, right_gloves)  # solution함수에 left_gloves의 값과 right_gloves의 값을 넣어서 실행하기

print("solution 함수의 반환 값은", ret, "입니다.")  # 결과 출력하기

########################################################################################################################
# 문제 2번
def func_a(arr):  # func_a라는 함수 만들기
    count = 0  # 숫자를 저장할 count변수 만들기
    for n in arr:  # arr의 값을 n에 하나씩 대입하면서 반복하기
        if n % 5 == 0:  # 만약 n을 5로 나눴을 때의 나머지가 0이라면
            count += 1  # count에 1을 더하기
    return count  # count의 값을 반환하기

def func_b(three, five):  # func_b라는 함수 만들기
    if three > five:  # 만약 three가 five보다 크다면
        return "three"  # three라는 문자열을 반환하기
    elif three < five:  # 만약 five가 three보다 크다면
        return "five"  # five라는 문자열을 반환하기
    else:               # 만약 둘다 아니라면
        return "same"  # same이라는 문자열을 반환하기

def func_c(arr):  # func_c라는 함수를 만들기
    count = 0  # 숫자를 저장할 count변수 만들기
    for n in arr:  # arr의 값을 차례로 n에 넣어서 반복하기
        if n % 3 == 0:  # 만약 n을 3으로 나눈 나머지가 0이라면
            count += 1  # count에 1을 더하기
    return count  # count의 값을 반환하기

def solution(arr):  # solution 함수 만들기
    count_three = func_c(arr)  # count_three에 arr의 값을 func_c에 넣은 값을 저장하게 하기
    count_five = func_a(arr)   # count_five에 arr의 값을 func_a에 넣은 값을 저장하게 하기
    answer = func_b(count_three, count_five)  # answer을 func_b에 count_three의 값과 count_five의 값을 넣은 값을 저장하기
    return answer  # answer의 값을 반환 하기

arr = [2, 3, 6, 9, 12, 15, 10, 20, 22, 25]  # 숫자가 들어있는 arr 리스트 만들기
ret = solution(arr)  # solution에 arr의 값을 넣고 함수 실행하기

print("solution 함수의 반환 값은", ret, "입니다.")  # 결과 출력하기

#######################################################################################################################
# 문제 3번
def solution(N, M):  # solution 함수 만들기
    answer = 0  # 총합을 저장할 answer 변수
    for i in range(N, M): # N의 값부터 M의 값까지 1씩 더하면서 i에 대입
        if i % 2 == 0:  # 만약 i 나누기 2의 나머지가 0 이라면
            answer += i * i  # answer의 i의 제곱값을 더하기
    return answer  # answer의 값을 반환하기

N = 4  # 정수를 저장할 N 변수
M = 7  # 정수를 저장할 M 변수
ret = solution(N, M)  # solution 함수에 N과 M을 넣어 실행한 뒤 그 값을 ret에 저장

print("solution 함수의 반환 값은", ret, "입니다.")  # 결과 출력하기

#######################################################################################################################
# 문제 4번
def solution(words):  # solution 함수 만들기
    answer = ''  # 문자를 담는 answer 변수 만들기
    count = 0  # 숫자를 저장하는 count변수 만들기
    for i in words:  # words의 값을 차례로 i에 집어 넣으면서 반복 하기
        if len(i) >= 5:  # 만약 i의 단어 길이가 5 이상이라면
            answer += i  # answer에 i의 단어를 넣기
    if answer == '':  # 만약 answer이 비어 있다면
        answer = "empty"  # answer의 값을 empty로 하기
    return answer  # answer의 값을 반환하기

words1 = ["my", "favorite", "color", "is", "violet"]  # 단어들이 들어있는 words1 리스트
ret1 = solution(words1);  # words1을 solution 함수에 넣으면서 실행 후 ret1에 그 값을 저장하기

print("solution 함수의 반환 값은 ", ret1, " 입니다.")  # 결과 출력하기

words2 = ["yes", "i", "am"]  # 단어들이 들어있는 words2리스트
ret2 = solution(words2);  # words2을 solution 함수에 넣으면서 실행 후 ret2에 그 값을 저장하기

print("solution 함수의 반환 값은 ", ret2, " 입니다.")  # 결과 출력하기
#######################################################################################################################
# 문제 5번
def solution(attack, recovery, hp):  # solution 함수 만들기
    count = 0  # 공격 횟수를 셀 count 변수
    while(True):  # 무한 반복하기
        count += 1  # 공격 횟수 1회 더하기
        hp -= attack  # hp에 attack만큼 깎기
        if hp <= 0:  # 만약 hp가 0보다 작거나 같다면
            break  # 멈추기
        hp += recovery  # recovery만큼 회복하기
    return count  # 공격 횟수 반환하기

attack = 30  # 공격력을 저장할 attack 변수
recovery = 10  # 체력 재생을 저장할 recovery 변수
hp = 60  # 체력을 저장할 hp 변수
ret = solution(attack, recovery, hp)  # hp, attack, recovery를 solution함수에 넣어 실행한 후 ret에 저장하기

print("solution 함수의 반환 값은", ret, "입니다.")  # 결과 출력하기

#######################################################################################################################
# 문제 6번
def solution(floors):  # solution 함수 만들기
    dist = 0  # 이동거리를 저장할 dist변수 만들기
    length = len(floors)  # lennth에 floors의 길이를 저장하기
    for i in range(1, length):  # 1부터 length의 값까지 1씩 더하면서 반복
        if floors[i] > floors[i - 1]:  # 만약 i번째 floors가 i - 1 번째 floors보다 크다면
            dist += floors[i] - floors[i-1]  # dist에 i번째 floors 에 i - 1번째 floors를 빼기
        else:  # 아니라면
            dist += floors[i-1] - floors[i]  # dist에 i - 1번째 floors 에 i번째 floors를 빼기
    return dist  # dist의 값을 반환하기

floors = [1, 2, 5, 4, 2]  # 이동 층수를 저장하는 floors 변수
ret = solution(floors)  # solution에 floors를 넣어서 ret에 저장하가ㅣ

print("solution 함수의 반환 값은", ret, "입니다.")  # 결과 출력하기

######################################################################################################################
# 문제 7번
def solution(value, unit):  # solution 함수 만들기
    converted = 0  # 정수를 저장하는 converted 변수 만들기
    if unit == "C":  # 만약 unit의 값이 "C"라면
        value = value * 1.8 + 32  # value의 값은 value * 1.8 + 32로 하기
    if unit == "F":  # 만약 unit의 값이 "F"라면
        value = (value - 32) / 1.8  # value의 값은 (value -32) / 1.8로 하기
    converted = int(value)  # converted에 value의 값 정수 형태로 대입하기
    return converted  # converted의 값을 반환하기

value = 527  # 화씨온도를 저장하는 value 변수
unit = "C"  # Unit을 저장하는 unit변수
ret = solution(value, unit)  # solution에 value와 unit을 넣어서 함수 실행한 뒤 ret에 저장

print("solution 함수의 반환 값은", ret, "입니다.")  # 결과 출력하기
######################################################################################################################
# 문제 8번
def solution(number):
    count = 0
    while number != 0:
        n = number % 10
        if n == 2 or n == 3 or n == 5 or n == 7:
            count += 1
        number //= 10
    return count

number = 29022531
ret = solution(number)

print("solution 함수의 반환 값은", ret, "입니다.")
######################################################################################################################
# 문제 9번
def solution(votes, N, K):
    counter = [0 for _ in range(N + 1)]
    for x in votes:
        counter[x] += 1
    answer = 0
    for c in counter:
        if c == K:
            answer += 1
    return answer

votes = [2, 5, 3, 4, 1, 5, 1, 5, 5, 3]
N = 5
K = 2
ret = solution(votes, N, K)

print("solution 함수의 반환 값은", ret, "입니다.")
######################################################################################################################
# 문제 10번
def solution(purchase):
    total = 0
    for p in purchase:
        if p >= 1000000:
            total += 50000
        elif p >= 600000:
            total += 30000
        elif p >= 400000:
            total += 20000
        elif p >= 200000:
            total += 10000
    return total

purchase = [150000, 210000, 399990, 990000, 1000000]
ret = solution(purchase)

print("solution 함수의 반환 값은", ret, "입니다.")