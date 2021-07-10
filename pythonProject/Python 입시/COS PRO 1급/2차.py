# 1번
from abc import *

class Book(metaclass=ABCMeta):
    @abstractmethod
    def get_rental_price(self, day):
        pass

class ComicBook(Book):
    def get_rental_price(self, day):
        cost = 500
        day -= 2
        if day > 0:
            cost += day * 200
        return cost


class Novel(Book):
    def get_rental_price(self, day):
        cost = 1000
        day -= 3
        if day > 0:
            cost += day * 300
        return cost


def solution(book_types, day):
    books = []
    for types in book_types:
        if types == "comic":
            books.append(ComicBook())
        elif types == "novel":
            books.append(Novel())
    total_price = 0
    for book in books:
        total_price += book.get_rental_price(day)
    return total_price


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
book_types = ["comic", "comic", "novel"]
day = 4
ret = solution(book_types, day)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
#######################################################################################################################
# 2번
def func_a(times):
    hour = int(times[:2])
    minute = int(times[3:])
    return hour*60 + minute

def solution(subway_times, current_time):
    current_minute = func_a(current_time)
    INF = 1000000000
    answer = INF
    for s in subway_times:
        subway_minute = func_a(s)
        if subway_minute >= current_minute:
            answer = subway_minute - current_minute
            break
    if answer == INF:
        return -1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.

subway_times1 = ["05:31", "11:59", "13:30", "23:32"]
current_time1 = "12:00"
ret1 = solution(subway_times1, current_time1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

subway_times2 = ["14:31", "15:31"]
current_time2 = "15:31"
ret2 = solution(subway_times2, current_time2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
# #######################################################################################################################
# # 3번
def func_a(n):
    ret = 1
    while n > 0:
        ret *= 10
        n -= 1
    return ret


def func_b(n):
    ret = 0
    while n > 0:
        ret += 1
        n //= 10
    return ret


def func_c(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret


def solution(num):
    next_num = num
    while True:
        next_num += 1
        length = func_b(next_num)
        if length % 2:
            continue

        divisor = func_a(length // 2)

        front = next_num // divisor
        back = next_num % divisor

        front_sum = func_c(front)
        back_sum = func_c(back)
        if front_sum == back_sum:
            break

    return next_num - num


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
num1 = 1
ret1 = solution(num1)
#######################################################################################################################
# # 4번
# def solution(arr, K):
#     answer = 0
#     num = 1
#     for i in arr:
#
#     return answer
#
# arr = [1, 2, 3, 4, 5]
# K = 3
# ret = solution(arr, K)
#
# print("solution 함수의 반환 값은 ", ret, " 입니다.")
# #######################################################################################################################
# # 5번
# #다음과 같이 import를 사용할 수 있습니다.
# #import math
#
# def solution(arr):
#     #여기에 코드를 작성해주세요.
#     answer = 0
#     return answer
#
# #아래는 테스트케이스 출력을 해보기 위한 코드입니다.
# arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
# ret = solution(arr)
#
#
# #[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret, "입니다.")
# #######################################################################################################################
# # 6번

def solution(commands):
    current_position = [0, 0]
    for d in commands:
        if d == "L":
            current_position[0] -= 1
        elif d == "R":
            current_position[0] += 1
        elif d == "U":
            current_position[1] += 1
        elif d == "D":
            current_position[1] -= 1
    return current_position

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
commands = "URDDL"
ret = solution(commands)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
# #######################################################################################################################
# 7번
def solution(money):
    coin = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
    counter = 0
    idx = len(coin) - 1
    while money:
        counter += money // coin[idx]
        money %= coin[idx]
        idx -= 1
    return counter

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
money = 2760
ret = solution(money)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
# #######################################################################################################################
# 8번
def solution(arr):
    left, right = 0, len(arr) - 1
    idx = 0
    answer = [0 for _ in range(len(arr))]
    while left <= right:
        if idx % 2 == 0:
            answer[idx] = arr[left]
            left += 1
        else:
            answer[idx] = arr[right]
            right -= 1
        idx += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution 함수만 수정하세요.
arr = [1, 2, 3, 4, 5, 6]
ret = solution(arr)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
# #######################################################################################################################
# 9번
def solution(password):
    length = len(password)
    for i in range(length - 2):
        first_check = ord(password[i + 1]) - ord(password[i])
        second_check = ord(password[i + 2]) - ord(password[i+1])
        if first_check == second_check and (first_check == 1 or first_check == -1):
            return False
    return True

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
password1 = "cospro890"
ret1 = solution(password1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

password2 = "cba323"
ret2 = solution(password2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
# #######################################################################################################################
# 10번
def solution(s):
    s += '#'
    answer = ""
    for i in range(len(s)):
        if s[i] == '0' and s[i + 1] != '0':
            answer += '0'
        elif s[i] == '1':
            answer += '1'
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
s = "101100011100"
ret = solution(s)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")