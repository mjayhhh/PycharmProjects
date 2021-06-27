# 1번
print("-----1번-----")
def func_a(k):                  # 1부터 k까지의 숫자의 합을 구하는 함수
    sum = 0
    for i in range(1, k + 1):
        sum += i
    return sum

def solution(n, m):             # 답을 구하는 함수
    sum_to_m = func_a(m)        # 1부터 m까지의 합을 구하는 문장
    sum_to_n = func_a(n-1)      # 1부터 n-1까지 합을 구하는 문장
    answer = sum_to_m - sum_to_n    # 답을 구하기
    return answer   # 답 반환하기

# def func_a(k):
#     sum = 0
#     for i in range(k):
#         sum += i+1
#     return sum
#
# def solution(n, m):
#     sum_to_m = func_a(m)
#     sum_to_n = func_a(n-1)
#     answer = sum_to_m - sum_to_n
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
def func_a(s):
    ret = 0
    for i in s:
        if i > ret:
            ret = i
    return ret

def func_b(s):
    ret = 0
    for i in s:
        ret += i
    return ret

def func_c(s):
    ret = 101
    for i in s:
        if i < ret:
            ret = i
    return ret


def solution(scores):
    sum = func_b(scores)
    max_score = func_a(scores)
    min_score = func_c(scores)
    return sum - max_score - min_score

scores = [50, 35, 78, 91, 85]
ret = solution(scores)
print(ret)
########################################################################################################################
# 3번
print("-----3번-----")
def func_a(arr, n):
    ret = []
    for x in arr:
        if x != n:
            ret.append(x)
    return ret

def func_b(a, b):
    if a >= b:
        return a - b
    else:
        return b - a

def func_c(arr):
    ret = -1
    for x in arr:
        if ret < x:
            ret = x
    return ret

def solution(visitor):
    max_first = func_c(visitor)
    visitor_removed = func_a(visitor, max_first)
    max_second = func_c(visitor_removed)
    answer = func_b(max_first, max_second)
    return answer

visitor = [4,7,2,9,3]
ret = solution(visitor)
print(ret)
########################################################################################################################
# 4번
print("-----4번-----")
def solution(scores):
    grade_counter = [0 for i in range(5)]
    for x in scores:
        if x >= 85:
            grade_counter[0] += 1
        elif x >= 70:
            grade_counter[1] += 1
        elif x >= 55:
            grade_counter[2] += 1
        elif x >= 40:
            grade_counter[3] += 1
        else:
            grade_counter[4] += 1
    return grade_counter

# def solution(scores):
#     grade_counter = [0 for i in range(5)]
#     for x in scores:
#         if x >= 85:
#             grade_counter[0] += 1
#         elif x < 85 and x >= 70:
#             grade_counter[1] += 1
#         elif x < 70 and x >= 55:
#             grade_counter[2] += 1
#         elif x < 55 and x >= 40:
#             grade_counter[3] += 1
#         else:
#             grade_counter[4] += 1
#     return grade_counter

scores = [86,72,98,60,45]
ret = solution(scores)
print(ret)
########################################################################################################################
# 5번
print("-----5번-----")
def solution(stones):
    cnt = 0
    current = 0
    n = len(stones)
    while current <= n - 1:
        current += stones[current]
        cnt += 1
    return cnt

stones = [2,5,1,3,2,1]
ret = solution(stones)
print(ret)
########################################################################################################################
# 6번
print("-----6번-----")
def solution(height, k):
    answer = 0
    n = len(height)
    for h in height:
        if h > k:
            answer += 1
    return answer

height = [165, 170, 175, 180, 184]
k = 175
ret = solution(height, k)
print(ret)
########################################################################################################################
# 7번
print("-----7번-----")
def solution(s):
    s_lst = list(s)
    n = len(s)
    for i in range(n):
        if s_lst[i] == 'a':
            s_lst[i] = 'z'
        elif s_lst[i] == 'z':
            s_lst[i] =  'a'
    return "".join(s_lst)

s = "abz"
ret = solution(s)
print(ret)
########################################################################################################################
# 8번
print("-----8번-----")
def solution(name_list):
    answer = 0
    for name in name_list:
        for n in name:
            if n == 'j' or n == 'k':
                answer += 1
                break
    return answer

name_list = ["james", "luke", "oliver", "jack"]
ret = solution(name_list)
print(ret)
########################################################################################################################
# 9번
print("-----9번-----")
def solution(price, money):
    answer = 0
    for i in price :
        answer += i
    if answer <= money :
        answer = money - answer
    else :
        answer = -1
    return answer

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
    list.sort(reverse=False)    # 반대로 뒤집기
    answer = list[k - 1]
    return answer

# def solution(arr, k):
#     return sorted([n for seq in arr for n in seq])[k - 1]

arr = [[5,12,4,31],[24,13,11,2],[43,44,19,26],[33,65,20,21]]
k = 4
ret = solution(arr, k)

print(ret)