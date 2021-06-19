# 1번
def solution(ladders, win):
    answer = 0
    player = [1, 2, 3, 4, 5, 6]
    for e in ladders:
        temp = player[e[0]-1]
        player[e[1] - 1] = temp

        win = temp
    answer = player[win-1]
    return answer

ladders = [[1, 2], [3, 4], [2, 3], [4, 5], [5, 6]]
win = 3
ret = solution(ladders, win)

print("solution 함수의 반환 값은", ret, "입니다.")
# 내려오는 두 사람의 위치를 맨위에서 부터 바꿔서 win이랑 맞는 사람의 위치를 출력
#####################################################################################################################
# 2번
def func_a(time_table):
    answer = 0
    for i, t in reversed(list(enumerate(time_table))):
        if t == 1:
            answer = i
            break
    return answer

def func_b(time_table, class1, class2):
    answer = 0
    for i in range(class1, class2):
        if time_table[i] == 0:
            answer += 1
    return answer

def func_c(time_table):
    answer = 0
    for i, t in enumerate(time_table):
        if t == 1:
            answer = i
            break
    return answer

def solution(time_table):
    answer = 0
    first_class = func_c(time_table)
    last_class = func_a(time_table)
    answer = func_b(time_table, first_class, last_class)
    return answer

time_table = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
ret = solution(time_table)

print("solution 함수의 반환 값은", ret, "입니다.")
#####################################################################################################################
# 3번
def solution(speed, cars):
    answer = 0
    for x in cars:
        if x >= speed * 11 / 10 and x < speed * 12 / 10:
            answer += 3
        elif x >= speed * 1.2 and x < speed * 1.3:
            answer += 5
        elif x >= speed * 1.3:
            answer += 7
    return answer

speed = 100
cars = [110, 98, 125, 148, 120, 112, 89]
ret = solution(speed, cars)

print("solution 함수의 반환 값은", ret, "입니다.")
#####################################################################################################################
# 4번
def solution(taekwondo, running, shooting):
    answer = 0
    if taekwondo >= 25:
    	answer += 250
    else:
    	answer += taekwondo * 8
    answer += 250 + (60 - running) * 5
    count = 0
    for s in shooting:
    	answer += s
    	if s == 10:
    		count += 1
    if count >= 7:
    	answer += 100
    return answer

taekwondo = 27
running = 63
shooting = [9, 10, 8, 10, 10, 10, 7, 10, 10, 10]
ret = solution(taekwondo, running, shooting)

print("solution 함수의 반환 값은", ret, "입니다.")
#####################################################################################################################
# 5번
def solution(a, b):
    answer = 0
    for i in range(1, b + 1):
        if (a * i) % b == 0:
            answer = a * i
            break
    return answer

a = 4
b = 6
ret = solution(a, b)

print("solution 함수의 반환 값은", ret, "입니다.")
#####################################################################################################################
# 6번
def solution(korean, english):
    answer = 0
    math = 210 - korean - english
    if math > 100:
        answer = -1
    else:
        answer = math
    return answer

korean = 70
english = 60
ret = solution(korean, english)

print("solution 함수의 반환 값은", ret, "입니다.")
#####################################################################################################################
# 7번
def solution(stuffs):
    answer = 0
    small_counter, general_counter = 0, 0
    for s in stuffs:
        if s > 3:
            general_counter += s
        else:
            small_counter += s
    if small_counter > general_counter:
        answer = small_counter
    else:
        answer = general_counter
    return answer

stuffs = [5, 3, 4, 2, 3, 2]
ret = solution(stuffs)

print("solution 함수의 반환 값은 ", ret, " 입니다.")
#####################################################################################################################
# 8번
def solution(usage):
    answer = 0
    if usage > 30:
        answer = 20 * 430 + 10 * 570 + (usage - 30) * 840
    elif usage > 20:
        answer = 20 * 430 + (usage - 20) * 570
    else:
        answer = usage * 430
    return answer

usage = 35
ret = solution(usage)

print("solution 함수의 반환 값은", ret, "입니다.")
#####################################################################################################################
# 9번
def solution(score):
    list = []
    for a in score:
        list.append(a)
    length = len(score)
    list.sort(reverse=True)
    num = []
    for a in range(length) :
        for i in range(length) :
            if a != i :
                if list[a] == list[i]:
                    num.append(list[a])
    for i in range(len(score)):
        for a in range(len(list)):
            if list[a] == score[i]:
                score[i] = a + 1
    answer = score
    return answer

score1 = [90, 87, 87, 23, 35, 28, 12, 46]
ret1 = solution(score1)

print("solution 함수의 반환 값은 ", ret1, " 입니다.")

score2 = [10, 20, 20, 30]
ret2 = solution(score2)

print("solution 함수의 반환 값은 ", ret2, " 입니다.")
#####################################################################################################################
# 10번

def solution(time_table, n):
    answer = 0
    time = [0 for _ in range(n)]
    count = 0
    for i in time_table:
        if count > n - 1:
            count = 0
        time[count] += i
        count += 1
    time.sort(reverse=True)
    answer = time[0]
    return answer

time_table1 = [1, 5, 1, 9]
n1 = 3
ret1 = solution(time_table1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

time_table2 = [4, 8, 2, 5, 4, 6, 7]
n2 = 4
ret2 = solution(time_table2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")