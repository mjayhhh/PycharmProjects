# 1번. n번째에서 n을 입력받고 n번 학생이 몇등인지 구하기
def func_a(scores, score):      # scores랑 score을 담는 func_a 함수 만들기
    rank = 1                    # rank 1로 설정하기
    for s in scores:            # scores리스트를 s에 넣어서 반복하기
        if s == score:          # 만약 score이랑 s의 값이 같다면
            return rank         # rank 돌려주기
        rank += 1               # 아니라면 rank에 1더해주기
    return 0                    # 0 돌려주기

def func_b(arr):  # 점수를 큰 순서대로 만드는 func_b 함수
    arr.sort(reverse=True)  # arr을 내림차순으로 만들기

def func_c(arr, n):  # arr과 n을 입력받은 func_c 함수 만들기
    return arr[n]   # arr리스트에서 n번째 값을 불러오기

def solution(scores, n):  # scores와 n을 입력받은 solution 함수 만들기
    score = func_c(scores, n)  # 그 학생의 점수를 저장하는 score변수
    func_b(scores)  # scores리스트를 큰 순서대로 만드는 문장
    answer = func_a(scores, score)  # 답을 저장하는 answer변수
    return answer  # 답의 값을 보냄

scores = [20, 60, 98, 59]  # 학생들의 점수를 담고 있는 scores리스트
n = 3   # 몇번째 학생의 등수를 출력할지 알려주는 n변수
ret = solution(scores, n)   # 그 값을 만드는 solution함수를 호출한뒤 그 값을 ret에 저장하는 문장

print("solution 함수의 반환 값은", ret, "입니다.") # 결과를 출력
######################################################################################################################
# 2번.장학금을 받는 장학생이 몇명인지 구하기
def func_a(current_grade, last_grade, rank, max_diff_grade):  # 학생의 최고 점수를 구하는 func_a함수 만들기
    arr_length = len(current_grade)  # arr_length를 current_grade의 길이로 정하기
    count = 0   # count를 0으로 정하기
    for i in range(arr_length):  # arr_length만큼 반복하기
        if current_grade[i] >= 80 and rank[i] <= arr_length // 10:   # 만약 current_grade의 1번째 학생이 80점 보다 높고 i번째 rank의 값이 arr_length에 10을 나눈거 보다 작거나 같다면
            count += 1  # count에 1을 더하기
        elif current_grade[i] >= 80 and rank[i] == 1:   # 만약 current_grade의 i번째 같이 80보다 크거나 같고 rank의 i번째가 1이랑 같다면
            count += 1  # count에 1을 더하기
        elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]: # 만약 max_diff_grade가 0보다 크고 max_diff_grade가 current_grade의 1번째에 last_grade의 i번째를 뺀 값과 같다면
            count += 1  # 1을 더하기
    return count    # count를 반환하기

def func_b(current_grade):      # 각 학생들의 점수를 구하는 func_b함수
    arr_length = len(current_grade)  # arr_length를 current_grade의 길이의 리스트로 하기
    rank = [1] * arr_length     # rank의 arr_length의 길이만큼 리스트를 만들기
    for i in range(arr_length):     # arr_length의 길이만큼 반복하기
        for j in range(arr_length):    # arr_length만큼 반복하기
            if current_grade[i] < current_grade[j]:     # 만약에 current_grade의 i번째 값이 current_grade의 j번째 값보다 낮다면
                rank[i] += 1       # rank에 1을 더하기
    return rank     # rank반환하기

def func_c(current_grade, last_grade):      # 학생들의 저번 시험 점수와 이번 시험 점수의 석차가 가장 큰 학생을 구하는 func_c함수
    max_diff_grade = 1      # max_diff_grade를 1로 정하기
    for i in range(len(current_grade)):     # current_grade의 길이만큼 반복하기
        max_diff_grade = max(max_diff_grade, current_grade[i] - last_grade[i])  # 지금까지 나온 석차가 가장 큰 학생과 이번에 나온 석차를 비교해서 더 큰걸 저장
    return max_diff_grade   # max_diff_grade의 값을 반환하기

def solution(current_grade, last_grade):    # 장학생의 수를 구하는 solution함수
    rank = func_b(current_grade)    # 학생의 등수를 알아내는 문장
    max_diff_grade = func_c(current_grade, last_grade)  # 석차가 가장 큰 학생을 알아내는 문장
    answer = func_a(current_grade, last_grade, rank, max_diff_grade)    # 장학생의 수를 모두 구하는 문장
    return answer   # answer의 값을 반환

current_grade = [70, 100, 70, 80, 50, 95]   # 애들의 최근 점수가 들어있는 current_grade 리스트
last_grade = [35, 65, 80, 50, 20, 60]   # 애들의 저번 성적이 들어있는 last_grade 리스트
ret = solution(current_grade, last_grade)   # 장학생의 수를 구하고 그 값을 저장하는 ret변수

print("solution 함수의 반환 값은", ret, "입니다.")    # 답을 출력
######################################################################################################################
# 3번. 가장 높은 점수 하나랑 가장 낮은 점수 하나를 제외한 나머지의 점수들의 평균을 계산하기
def solution(scores):   # 평균을 구하는 solution함수
    answer = 0  # answer을 0으로 하기
    scores.sort(reverse=True)   # scores리스트를 내림차순으로 만들기
    for i in range(1, len(scores) - 1):  # 1부터 scores의 길이의 1을 뺀 값까지 i에 1씩 더하면서 반복
        answer += scores[i]    # answer에 scores의 i번째 값을 더하기
    answer = answer / (len(scores) - 2)  # answer에 평균을 넣기
    return int(answer)  # int형의 answer을 반환하기

scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]   # 점수가 들어있는 scores1리스트
ret1 = solution(scores1)    # 평균을 구하고 그 값을 저장하는 ret1변수

print("solution 함수의 반환 값은", ret1, "입니다.")   # 결과를 출력

scores2 = [1, 1, 1, 1, 1]   # 점수가 들어있는 scores2리스트
ret2 = solution(scores2)    # socres2의 평균을 구하고 그 값을 저장하는 ret2변수

print("solution 함수의 반환 값은", ret2, "입니다.")   # 결과값을 반환하기
######################################################################################################################
# 4번. 지정한 단어가 있고 거기에 쓴 단어들이 word와 다른 문자의 개수를 구하기
def solution(words, word):  # 틀린 개수를 구하는 solution 함수
    count = 0   # count를 0으로 하기
    b = 0   # b를 0으로 하기
    for i in words:  # wrods의 값을 i 에 넣은면서 반복하기
        for a in range(4):  # 0부터 3까지 1씩 증가하면서 반복
            if word[a] != i[a]:   # 만약 words의 a번째의 값이 i의 a번째의 값과 다르다면
                count += 1  # count에 1을 더하기
        b = 0   # b를 다시 0으로 설정하기

    return count    # count의 값을 반환하기

words = ["CODE", "COED", "CDEO"]    # 어떤 사람이 쓴 단어가 들어있는 words리스트
word = "CODE"   # 지정한 단어를 저장하고 있는 word변수
ret = solution(words, word) # 틀린 개수를 구하고 그 값을 저장하는 ret변수

print("solution 함수의 반환 값은", ret, "입니다.")    # 결과값을 출력함
######################################################################################################################
# 5번. 사람들의 총 가격을 구하기( 이때 10명 이상일때는 할인이 있음 )
def solution(member_age, transportation):   #
	if transportation == 'Bus':
		adult_expense = 40000
		child_expense = 15000
	elif transportation == 'Ship':
		adult_expense = 30000
		child_expense = 13000
	elif transportation == 'Airplane':
		adult_expense = 70000
		child_expense = 45000

	if len(member_age) >= 10:
		adult_expense = adult_expense * 0.9
		child_expense = child_expense *  0.8

	total_expenses = 0
	for age in member_age:
		if age >= 20:
			total_expenses += adult_expense
		else:
		 total_expenses += child_expense

	return total_expenses

member_age1 = [13, 33, 45, 11, 20]
transportation1 = "Bus"
ret1 = solution(member_age1, transportation1)

print("solution 함수의 반환 값은", ret1, "입니다.")

member_age2 = [25, 11, 27, 56, 7, 19, 52, 31, 77, 8]
transportation2 = "Ship"
ret2 = solution(member_age2, transportation2)

print("solution 함수의 반환 값은", ret2, "입니다.")
######################################################################################################################
# 6번
def solution(tile_length):
    answer = ''
    com = 'RRRGGB'
    if tile_length%6 == 1 or tile_length%6 == 2 or tile_length % 6 == 4:
        answer = '-1'
    else:
        for i in range(tile_length):
            answer += com[i % 6]
    return answer

tile_length1 = 11
ret1 = solution(tile_length1)

print("solution 함수의 반환 값은 ", ret1, " 입니다.")

tile_length2 = 16
ret2 = solution(tile_length2)

print("solution 함수의 반환 값은 ", ret2, " 입니다.")
######################################################################################################################
# 7번
def solution(num_apple, num_carrot, k):
    answer = 0

    if num_apple < num_carrot * 3:
        answer = num_apple // 3
    else:
        answer = num_carrot

    num_apple -= answer * 3
    num_carrot -= answer

    i = 0
    while k - (num_apple + num_carrot + i) > 0:
        if i % 4 == 0:
            answer -= 1
        i = i + 1

    return answer

num_apple1 = 5
num_carrot1 = 1
k1 = 2
ret1 = solution(num_apple1, num_carrot1, k1)

print("solution 함수의 반환 값은", ret1, "입니다.")

num_apple2 = 10
num_carrot2 = 5
k2 = 4
ret2 = solution(num_apple2, num_carrot2, k2)

print("solution 함수의 반환 값은", ret2, "입니다.")
######################################################################################################################
# 8번
def solution(programs):
    answer = 0
    used_tv = [0] * 25

    for program in programs:
        for i in range(program[0], program[1]):
            used_tv[i] = used_tv[i] + 1

    for i in used_tv:
        if i >= 2:
            answer = answer + 1
    return answer

programs = [[1, 6], [3, 5], [2, 8]]
ret = solution(programs)

print("solution 함수의 반환 값은", ret, "입니다.")
######################################################################################################################
# 9번
def solution(day, numbers):
    count = 0
    for number in numbers:
        if number % 2 == day % 2:
            count += 1
    return count

day = 17
numbers = [3285, 1724, 4438, 2988, 3131, 2998]
ret = solution(day, numbers)

print("solution 함수의 반환 값은", ret, "입니다.")
######################################################################################################################
# 10번
def solution(arr):
    answer = 0
    for i in arr:
        if i/2 in arr:
            answer += 1
    return answer

arr = [4, 8, 3, 6, 7]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")