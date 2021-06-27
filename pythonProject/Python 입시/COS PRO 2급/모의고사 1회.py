# 1번
print("-----1번-----")
def func_a(k):                  # 1부터 k까지의 숫자의 합을 구하는 함수
    sum = 0
    for i in range(1, k + 1):   # 1부터 k까지 대입하면서 반복
        sum += i
    return sum

def solution(n, m):             # 답을 구하는 함수
    sum_to_m = func_a(m)        # 1부터 m까지의 합을 구하는 문장
    sum_to_n = func_a(n-1)      # 1부터 n-1까지 합을 구하는 문장
    answer = sum_to_m - sum_to_n    # 답을 구하기
    return answer   # 답 반환하기

# def func_a(k):
#     sum = 0
#     for i in range(k):    # 0부터 k까지 1씩 더하면서 반복
#         sum += i+1        # 총합에 i의 값에 1을 더한 값을 sum에 더하기
#     return sum
#
# def solution(n, m):
#     sum_to_m = func_a(m)      # 1부터 m까지의 합을 구하는 문장
#     sum_to_n = func_a(n-1)    # 1부터 n-1까지 합을 구하는 문장
#     answer = sum_to_m - sum_to_n  # 답 구하는 문장
#     return answer

n = 5
m = 10
ret = solution(n, m)
print(ret)

n = 6
m = 6
ret = solution(n, m)
print(ret)
########################################################################################################################
# 2번
print("-----2번-----")
def func_a(s):      # 가장 큰 값을 구하는 함수
    ret = 0
    for i in s:
        if i > ret: # 만약 i가 ret보다 크다면
            ret = i
    return ret

def func_b(s):     # 리스트의 총 합을 구하는 함수
    ret = 0
    for i in s:     # s의 값을 i에 대입 하면서 반복
        ret += i      # ret에 더하기
    return ret

def func_c(s):      # 가장 작은 값을 구하는 함수
    ret = 101
    for i in s:     # s의 값을 i에 대입하면서 반복
        if i < ret:  # 만ㅇ약 ret이 i보다 더 크다면
            ret = i
    return ret


def solution(scores):
    sum = func_b(scores)        # 총합 구하는 문장
    max_score = func_a(scores)  # 가장 큰 수 구하는 문장
    min_score = func_c(scores)  # 가장 작은 수 구하는 문장
    return sum - max_score - min_score  # 총합에 가장 큰수와 작은 수를 빼는 문장

scores = [50, 35, 78, 91, 85]
ret = solution(scores)
print(ret)
########################################################################################################################
# 3번
print("-----3번-----")
def func_a(arr, n):  # 리스트에 가장 큰 수를 뺴는 함수
    ret = []
    for x in arr:   # arr의 값을 x에 넣으면서 반복
        if x != n:  # 만약 x의 값이 n이랑 다르다면
            ret.append(x)   # ret리스트에 더하기
    return ret

def func_b(a, b):       # 큰 값에다가 작은 값을 빼는 함수
    if a >= b:      # 만약 A가 크거나 같다면 큰수에서 작은 수 빼기
        return a - b
    else:           # 아니라면
        return b - a

def func_c(arr):        # 가장 큰 값을 구하는 함수
    ret = -1
    for x in arr:
        if ret < x:         # 만약 x가 ret보다 크다면
            ret = x         # ret은 x로 정하기
    return ret

def solution(visitor):
    max_first = func_c(visitor)             # 가장 큰 수를 구하는 함수
    visitor_removed = func_a(visitor, max_first)    # 가장 큰수를 리스트에서 없애는 함수
    max_second = func_c(visitor_removed)        # 두번째로 큰 수를 구하는 함수
    answer = func_b(max_first, max_second)      # 가장 큰 수에 2번째로 큰 수를 빼는 문장
    return answer

visitor = [4,7,2,9,3]       # 방문자 수가 담겨있는 visitor 함수
ret = solution(visitor)
print(ret)
########################################################################################################################
# 4번
print("-----4번-----")
def solution(scores):
    grade_counter = [0 for i in range(5)]       # 0으로 된 리스트 5개 만들기
    for x in scores:        # scores의 값을 차례로 x에 대입하면서 반복
        if x >= 85:                     # 만약 점수가 85가 넘는다면
            grade_counter[0] += 1
        elif x >= 70:                   # 만약 점수가 70이 넘는다면
            grade_counter[1] += 1
        elif x >= 55:                   # 만약 점수가 55가 넘는다면
            grade_counter[2] += 1
        elif x >= 40:                   # 만약 점수가 40이 넘는다면
            grade_counter[3] += 1
        else:                           # 모두다 아니라면
            grade_counter[4] += 1
    return grade_counter

# def solution(scores):
#     grade_counter = [0 for i in range(5)]     # 0으로 된 리스트 5개 만들기
#     for x in scores:      # scores의 값을 차례로 x에 대입하면서 반복
#         if x >= 85:                   # 만약 점수가 85가 넘는다면
#             grade_counter[0] += 1
#         elif x < 85 and x >= 70:      # 만약 점수가 70이 넘는다면 또 점수가 85점 미만이라면
#             grade_counter[1] += 1
#         elif x < 70 and x >= 55:     # 만약 점수가 55가 넘는다면  또 점수가 70점 미만이라면
#             grade_counter[2] += 1
#         elif x < 55 and x >= 40:      # 만약 점수가 40이 넘는다면 또 점수가 55점 미만이라면
#             grade_counter[3] += 1
#         else:     # 만약 다 아니라면
#             grade_counter[4] += 1
#     return grade_counter

scores = [86,72,98,60,45]       # 점수가 담겨있는 scores함수
ret = solution(scores)
print(ret)
########################################################################################################################
# 5번
print("-----5번-----")
def solution(stones):
    cnt = 0
    current = 0
    n = len(stones)         # stones의 리스트의 길이를 저장하는 n 변수
    while current <= n - 1:         # n - 1이 current보다 클때는 계속 반복
        current += stones[current]  # current에 stones에 current번쨰값을 더하기
        cnt += 1    #  cnt에 1을 더하기
    return cnt

stones = [2,5,1,3,2,1]      # 건너는횟수가 담겨있는 stones함수
ret = solution(stones)
print(ret)
########################################################################################################################
# 6번
print("-----6번-----")
def solution(height, k):
    answer = 0           # k보다 큰 수의 개수
    n = len(height)      # 키의 목록 개수
    for h in height:         # 키 리스트를 하나씩 h에 대입
        if h > k:             # h가 k보다 더 크디먄
         answer += 1       # k보다 큰 수의 +1
    return answer
########################################################################################################################
# 7번
print("-----7번-----")


def solution(s):
    s_lst = list(s) # s_list에 s의 값을 리스트로 한 값을 대입
    n = len(s)  # n = 문자역 개수
    for i in range(n):  # 문자역 개수 반복
        if s_lst[i] == 'a':  # 만약에 리스트에[i] == 'a' 이면
            s_lst[i] = 'z'  # z 로 변경
        if s_lst[i] == 'z':  # 만약에 리스트에[i] = 'z' 이면
            s_lst[i] = 'a'  # 'a'로 변경

    return "".join(s_lst)  # " " 뒤에 문자열 붙이기
########################################################################################################################
# 8번
print("-----8번-----")
def solution(name_list):
    answer = 0  # 이름에 j , k 포함되어있는 학생수
    for name in name_list:  # 학생목록에 하나씩 name에 대입
        for n in name:  # name에 문자 하나씩 n에 대입
            if n == 'j' or n == 'k':    # 해당 문자가 j 또는 k 이면
                answer += 1  # 구하는 학생수에 +1
                break   # 반복문 멈추기
    # continue : 가장 가까운 for 다시 실행
    # break : 가장 가까운 for 종료
    return answer
########################################################################################################################
# 9번
print("-----9번-----")
def solution(price, money):
    answer = 0
    for i in price :   # price의 값을 i에 대입하면서 반복
        answer += i     # answer에 i의 값을 더하기
    if answer <= money :    # 만약에 낼 돈이 가격보다 큰다면
        answer = money - answer # 거스름돈 구하기
    else :  # 만약 아니라면
        answer = -1 # -1을 반환하기
    return answer   # 답 반환하기

# def solution(price, money):
#     return money-sum(price) if money>=sum(price) else -1

price = [2100, 3200, 2100, 800]
money = 10000
ret = solution(price, money)
print(ret)
########################################################################################################################
# 10번
print("-----10번-----")
def solution(arr, k):
    answer = 0
    list = []       # arr의 값을 1차원 리스트로 담을 list
    for a in arr :      # arr에 값을 a에 차례로 넣고
        for i in a :        # i에 a의 값을 차례로 넣음
            list.append(i)      # list에 i의 값을 넣기
    list.sort(reverse=False)    # 내림차순으로 만들기
    answer = list[k - 1]        # 리스트에 k번째로 큰 수를 대입하기
    return answer

# def solution(arr, k):
#     return sorted([n for seq in arr for n in seq])[k - 1]     # arr에 있는 값을 seq에 대입하면서 seq에 있는 값을 n에 넣으면서 그 n의 값으로 리스트를 만들고 그 만든 리스트를 내림차순으로 하며
# 그 리스트의 k번째로 큰 수를 구하기

arr = [[5,12,4,31],[24,13,11,2],[43,44,19,26],[33,65,20,21]]    # 숫자가 담겨있는 arr함수
k = 4
ret = solution(arr, k)

print(ret)