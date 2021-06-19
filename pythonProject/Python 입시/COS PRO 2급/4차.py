#######################################################################################################################
# 1번
def solution(schedule): # X의 개수를 구하는 함수
    answer = []
    for idx, i in enumerate(schedule):
        if i == "X":
            answer.append(idx + 1)
    return answer

schedule = ["O", "X", "X", "O", "O", "O", "X", "O", "X", "X"]   # O나 X를 쓴 학생들의 의견
ret = solution(schedule)

print("solution 함수의 반환 값은", ret, "입니다.")
#######################################################################################################################
# 2번
def func_a(passed, non_passed):
    return ( passed > 1 and non_passed ==0 )

def func_b(scores):
    answer = 0
    if scores[0] < 40:
        answer += 1
    if scores[1] < 44:
        answer += 1
    if scores[2] < 35:
        answer += 1
    return answer

def func_c(scores):
    answer = 0
    if scores[0] >= 80:
        answer += 1
    if scores[1] >= 88:
        answer += 1
    if scores[2] >= 70:
        answer += 1
    return answer

def solution(scores):
    answer = 0
    for my_score in scores:
        passed = func_c(my_score)
        non_passed = func_b(my_score)
        answer += func_a(passed, non_passed)
    return answer

scores1 = [[30, 40, 100], [97, 88, 95]]
ret1 = solution(scores1)

print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [[90, 88, 70], [85, 90, 90], [100, 100, 70], [30, 90, 80], [40, 10, 20], [83, 88, 80]]
ret2 = solution(scores2)

print("solution 함수의 반환 값은", ret2, "입니다.")
#######################################################################################################################
# 3번
def func_a(bundle, start):
    return bundle[start::2]

def func_b(score1, score2):
    if score1 > score2:
        return [1, score1]
    elif score2 > score1:
        return [2, score2]
    else:
        return [0, score1]

def func_c(bundle):
    answer = 0
    score_per_cards = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    }
    for card in bundle:
        answer += score_per_cards[card]
    return answer

def solution(n, bundle):
    a_cards = func_a(bundle, 0)[: n]
    b_cards = func_a(bundle, 1)[: n]
    a_score = func_c(a_cards)
    b_score = func_c(b_cards)
    return func_b(a_score, b_score)

n = 4
bundle = "cacdbdedccbb"
ret = solution(n, bundle)

print("solution 함수의 반환 값은", ret, "입니다.")
#######################################################################################################################
# 4번
def solution(classes, m):
    answer = 0
    for students in classes:
        answer += students // m
        if students % m != 0:
            answer += 1
    return answer

classes = [80, 45, 33, 20]
m = 30
ret = solution(classes, m)

print("solution 함수의 반환 값은", ret, "입니다.")
#######################################################################################################################
# 5번
def solution(calorie):
    min_cal = calorie[0]
    answer = 0
    for cal in calorie:
        if cal > min_cal:
            answer += cal - min_cal
        min_cal = min(min_cal, cal)
    return answer

calorie = [713, 665, 873, 500, 751]
ret = solution(calorie)

print("solution 함수의 반환 값은", ret, "입니다.")
#######################################################################################################################
# 6번
def solution(point):
    if point < 1000:
        return 0
    return point // 100 * 100

point = 2323
ret = solution(point)

print("solution 함수의 반환 값은", ret, "입니다.")
#######################################################################################################################
# 7번
def func_a(scores1, scores2):
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = max(answer, score2 - score1)
    return answer


def func_b(scores1, scores2):
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = min(answer, score2 - score1)
    return answer


def solution(mid_scores, final_scores):
    up = func_a(mid_scores, final_scores)
    down = func_b(mid_scores, final_scores)
    answer = [up, down]
    return answer

mid_scores = [20, 50, 40]
final_scores = [10, 50, 70]
ret = solution(mid_scores, final_scores)

print("solution 함수의 반환 값은", ret, "입니다.")
#######################################################################################################################
# 8번
def solution(n, votes):
    arr = [0] * (n + 1)
    for vote in votes:
        arr[vote] += 1

    for i in range(1, n +1):
        if arr[i] > len(votes)/2:
            return i
    return -1

n1 = 3
votes1 = [1, 2, 1, 3, 1, 2, 1]
ret1 = solution(n1, votes1)

print("solution 함수의 반환 값은 ", ret1, " 입니다.")

n2 = 2
votes2 = [2, 1, 2, 1, 2, 2, 1]
ret2 = solution(n2, votes2)

print("solution 함수의 반환 값은 ", ret2, " 입니다.")
#######################################################################################################################
# 9번
def solution(height):
    count = 0   # 위험지역의 총 개수
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):  # 4번 반복
        for a in range(4):  # 4번 반복
            위험지역 = True
            for k in range(4):
                if 0 <= i + dx[k] and i + dx[k] < 4 and 0 <= a + dy[k] and a + dy[k] < 4:
                    if height[i+dx[k]][a+dy[k]] <= height[i][a]:
                        위험지역 = False
            if 위험지역:
                count += 1
    return count

height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
ret = solution(height)

print("solution 함수의 반환 값은", ret, "입니다.")
#######################################################################################################################
def solution(scores, cutline):
    answer = 0
    for a in scores:
        if a >= cutline :
            answer += 1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [80, 90, 55, 60, 59]
cutline = 60
ret = solution(scores, cutline)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
########################################################################################################################