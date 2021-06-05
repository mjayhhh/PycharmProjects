# 문제 1

def solution(shirt_size): # solution 함수 만들기
    answer = [] # answer 변수 만들기
    size = ["XS", "S", "M", "L", "XL", "XXL"] # size 변수에 사이즈들을 저장
    for a in size : # size에 있는 값을 차례대로 a에 저장
        answer.append(shirt_size.count(a)) # 사이즈 작은 차례대로 개수를 세가지고 answer 리스트에 추가
    return answer # answer 값을 보내주기

shirt_size = ["XS", "S", "L", "L", "XL", "S"] # 학생들의 사이즈가 담겨있는 리스트
ret = solution(shirt_size); # solution 함수에 shirt_size를 넣어서 실행하기

print("Solution: return value of the function is ", ret, " .") # ret값을 넣어서 출력하기

#######################################################################################################################
# 문제 2
def solution(price, grade): # solution 함수 만들기
    answer = 0 # 깎인 가격을 저장할 함수
    if grade == "S" : # 만약 등급이 S라면
        answer = price * 0.95 # 5퍼센트 깎기
    elif grade == "G" : # 만약 등급이 G라면
        answer = price * 0.9 # 10퍼센트 깎기
    else : # 만약 둘다 아니라면
        answer = price * 0.85 # 15퍼센트 깎기
    return round(answer) # 반올림 한 상태로 answer값 보내주기

price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1) # 2500원과 V를 넣고 solution 함수 실행하기

print("Solution: return value of the function is", ret1, ".") # 결과값 출력하기

price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2) # 96900원과 S를 넣고 solution 함수 실행하기

print("Solution: return value of the function is", ret2, ".") # 결과값 출력하기

#######################################################################################################################
# 문제 3
def func_a(month, day): # func_a 함수 만들기
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 각 달의 일의 개수가 들어있는 리스트
    total = 0; # 일의 총합을 저장할 변수
    for i in range(month - 1): # month - 1의 값만큼 반복하기
        total += month_list[i] # total에 그동안 지났던 달의 일을 더해주기
    total += day # total에 지금의 일을 더하기
    return total - 1 # total에 1을 뺀 값을 보내주기


def solution(start_month, start_day, end_month, end_day): # solution 함수 만들기
    start_total = func_a(start_month, start_day) # start_month와 start_day를 넣어 func_a 실행하기
    end_total = func_a(end_month, end_day) # end_month와 end_day를 넣어 func_a 실행하기
    return end_total - start_total # 두개를 빼 두 날의 사이의 날 구하기

start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day) # 1, 2, 2, 2를 넣어 함수 실행하기

print("Solution: return value of the function is", ret, ".") # 결과값 출력하기

#######################################################################################################################
# 문제 4
def func_a(arr): # func_a라는 함수 실행하기
    counter = [0 for _ in range(1001)] # 각 함수들의 개수를 셀 counter 리스트
    for x in arr: # arr의 값을 x에 하나하나 대입하면서 반복하기
        counter[x] += 1 # 그런다음 그 값에 해당하는 자리에 1더하기
    return counter # counter 리스트를 보내주기

def func_b(arr): # 2단계 함수 : 가장 많이 등장하는 수 세기
    ret = 0 # 가장 많은 개수 가지고 있는 자연수를 저장하는 변수
    for x in arr: # x에 arr를 1개씩 대입하면서 반복
        if ret < x: # ret보다 개수를 더 많이 가지고 있다면
            ret = x # ret에 그 변수 대입하기
    return ret # ret를 보내주기

def func_c(arr): # 3단계 함수 : 가장 적게 등장하는 수 세기
    INF = 1001 # INF에 1001이 들어있는 변수
    ret = INF # ret에 INF의 값을 대입하기
    for x in arr: # x에 arr의 값을 넣어 반복하기
        if x != 0 and ret > x: # 만약 x의 값이 0이 아니고 ret이 x의 값보다 작으면
            ret = x # ret에 x의 값을 대입하기
    return ret # ret의 값을 보내주기

def solution(arr):
    counter = func_a(arr) # 각 자연수의 개수를 세기
    max_cnt = func_b(counter) # 가장 많이 등장하는 수를 max_cnt에 대입하기
    min_cnt = func_c(counter) # 가장 적게 등장하는 수를 min_cnt에 대입하기
    return max_cnt // min_cnt # max_cnt을 min_cnt으로 나누기(몫만)

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2] # 숫자들이 담겨있는 변수
ret = solution(arr) # arr에 값을 대입하면 solution 함수 실행하기

print("Solution: return value of the function is", ret, ".") # 결과값 출력하기

#######################################################################################################################
# 문제 5
def solution(arr): # solution 함수 만들기
    left, right = 0, len(arr)-1 # left에 0을 right에 3을 대입하기
    while left != 2 and right != 1: # left의 값이 2가 아니고 right의 값이 1이 아닐 동안 실행하기
        arr[left], arr[right] = arr[right], arr[left] # arr의 left번째의 값과 arr의 right번째의 값을 바꾸기
        left += 1 # left에 1을 더해주기
        right -= 1 # right에 1을 빼주기
    return arr # arr의 값을 보내주기

arr = [1, 4, 2, 3] # 숫자가 담겨있는 리스트
ret = solution(arr) # arr의 값을 대입해 solution 함수 실행하기

print("Solution: return value of the function is ", ret, " .") # 결과값 출력하기

#######################################################################################################################
# 문제 6
def solution(number): # solution 함수 만들기
    count = 0 # 박수를 친 횟수를 저장할 변수
    for i in range(1, number + 1): # 1부터 변수 + 1까지 만큼 i에 1씩 더하면서 반복
        current = i # current에 i를 대입
        temp = count # temp에 count를 대입
        while current != 0: # current가 0이 아닐 때 까지
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9: # 만약 current 나누기 10의 나머지가 3 또는 6 또는 9 이면
                count += 1 # 카운트에 1더하고 대입하기
                print("pair", end = '') # pair 출력하기
            current = current // 10 # current를 10으로 나누고 그 몫을 대입하기
        if temp == count: # 만약 temp랑 count가 같다면
            print(i, end = '') # i(숫자)를 출력하기
        print(" ", end = '') # 띄어주기
    print("") # 줄 바꿔주기
    return count # count값을 보내주기

number = 40
ret = solution(number) # solution에 40을 대입한후 함수를 실행하기

print("Solution: return value of the function is", ret, ".") # 결과 값 출력하기

#######################################################################################################################
# 문제 7
def solution(scores): # solution 함수 만들기
    count = 0 # 수강할 학생들의 수를 저장할 변수
    for s in scores: # scores의 값을 s에 하나하나 대입하면서 반복
        if 650 <= s and s < 800: # 만약 s가 650보다 크고 800보다 작다면
            count += 1 # count에 1을 더하고 대입하기
    return count # count의 값을 보내주기

scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores) # solution에 scores의 값을 대입한뒤 실행하기

print("Solution: return value of the function is", ret, ".") # 결과값 출력하기

#######################################################################################################################
# 문제 8
def solution(sentence):  # soulution이라는 함수 만들기
    str = ''  # 값을 저장하는 str변수 만들기
    for c in sentence:  # sentence의 값들을 차례로 c에 넣으면서 반복
        if c != '.' and c != ' ':  # 만약 그 c의 값이 .이거나 공백이 둘중의 하나라도 아니라면
            str += c  # str에 추가하기
    size = len(str)  # size를 str의 문자 길이로 정하기
    for i in range(size // 2):  # size의 길이의 반만큼 반복하기
        if str[i] != str[size - 1 - i]:  # 만약 str의 첫 문자와 끝 문자가 다르다면
            return False  # False 를 리턴하기
    return True  # 아니라면 True를 리턴하기

sentence1 = "never odd or even."  # 문자를 저장하는 sentence1변수 만들기
ret1 = solution(sentence1)  # sentence1을 넣어서 solution함수 실행하기

print("Solution: return value of the function is", ret1, ".")  # 결과 출력하기

sentence2 = "palindrome"   # 문자를 저장하는 sentence2변수 만들기
ret2 = solution(sentence2)  # sentence2을 넣어서 solution 함수 실행하기

print("Solution: return value of the function is", ret2, ".")  # 결과 출력하기

#######################################################################################################################
# 문제 9
def solution(characters):  # solution 이라는 함수 만들기
    result = ""  # 문자열을 저장할 result 함수를 만들기
    for i in range(len(characters)):  # characters의 길이 만큼 반복하기
        if characters[i - 1] != characters[i]:  # 만약 characters의 1칸 뒤의 문자랑 앞의 문자가 다르다면
            result += characters[i]  # result에 그 값을 넣기
    return result  # result 값 리턴하기

characters = "senteeeencccccceeee"  # 문자를 저장하는 characters변수 만들기
ret = solution(characters)  # characters을 넣어서 solution 함수 실행하기

print("Solution: return value of the function is", ret, ".")  # 결과 출력하기

#######################################################################################################################
# 문제 10
def solution(data):  # solution이라는 함수 만들기
    total = sum(data)  # data의 값의 합을 저장하는 total 변수 만들기
    average = total / len(data)  # data값의 평균을 구하는 average 변수 만들기
    cnt = 0  # 개수를 저장할 cnt변수
    for d in data:  # data의 값을 d에 차례로 넣으면서 반복
        if d <= average:  # 만약 d의 값이 평균보다 낮거나 같으면
            cnt += 1   # cnt에 1점 더하기
    return cnt  # cnt의 값을 리턴하기

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 숫자가 들어있는 data1리스트
ret1 = solution(data1)  # data1리스트를 solution에 넣어서 실행하기

print("Solution: return value of the function is", ret1, ".")  # 결과 출력하기

data2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]  # 숫자가 들어있는 data2리스트
ret2 = solution(data2)  # data2리스트를 solution에 넣어서 실행하기

print("Solution: return value of the function is", ret2, ".")  # 결과 출력하기