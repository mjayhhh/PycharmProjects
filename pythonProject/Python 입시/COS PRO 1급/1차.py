# 1번
from abc import *

class DeliveryStore(metaclass=ABCMeta):
    @abstractmethod
    def set_order_list(self, order_list):
        pass

    @abstractmethod
    def get_total_price(self):
        pass


class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class PizzaStore():
    def __init__(self):
        menu_names = ["Cheese", "Potato", "Shrimp", "Pineapple", "Meatball"]
        menu_prices = [11100, 12600, 13300, 21000, 19500];
        self.menu_list = []
        for i in range(5):
            self.menu_list.append(Food(menu_names[i], menu_prices[i]))

        self.order_list = []

    def set_order_list(self, order_list):
        for order in order_list:
            self.order_list.append(order)


    def get_total_price(self):
        total_price = 0
        for order in self.order_list:
            for menu in self.menu_list:
                if order == menu.name:
                    total_price += menu.price
        return total_price


def solution(order_list):
    delivery_store = PizzaStore()

    delivery_store.set_order_list(order_list)
    total_price = delivery_store.get_total_price()
    return total_price

# The following is code to output testcase.
order_list = ["Cheese", "Pineapple", "Meatball"]
ret = solution(order_list)

# Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
#######################################################################################################################
# 2번
def func_a(string, length):
    padZero = ""
    padSize = length - len(string)

    for i in range(padSize):
        padZero += "0"
    return padZero + string


def solution(binaryA, binaryB):
    max_length = max(len(binaryA), len(binaryB))
    binaryA = func_a(binaryA, max_length)
    binaryB = func_a(binaryB, max_length)

    hamming_distance = 0
    for i in range(max_length):
        if binaryA[i] != binaryB[i]:
            hamming_distance += 1
    return hamming_distance

# The following is code to output testcase.
binaryA = "10010"
binaryB = "110"
ret = solution(binaryA, binaryB)

# Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
#######################################################################################################################
# 3번
def func_a(numA, numB, exp):
    if exp == '+':
        return numA + numB
    elif exp == '-':
        return numA - numB
    elif exp == '*':
        return numA * numB


def func_b(exp):
    for index, value in enumerate(exp):
        if value == '+' or value == '-' or value == '*':
            return index


def func_c(exp, idx):
    numA = int(exp[:idx])
    numB = int(exp[idx + 1:])
    return numA, numB


def solution(expression):
    exp_index = func_b(expression)
    first_num, second_num = func_c(expression, exp_index)
    result = func_a(first_num, second_num, expression[exp_index])
    return result


# The following is code to output testcase.
expression = "123+12"
ret = solution(expression)

# Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
#######################################################################################################################
# 4번
def solution(num):
    answer = num + 1
    num2 = 1
    num3 = num + 1
    while num3 > 0 :
        if num3 % 10 == 0 :
            answer += num2
            num3 //= 10
            num2 *= 10
        else :
            num3 //= 10
            num2 *= 10
    return answer


#The following is code to output testcase.
num = 9949999;
ret = solution(num)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
#######################################################################################################################
# 5번
def solution(n):
    # Write code here.
    answer = 0
    return answer


# The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

n2 = 2
ret2 = solution(n2)

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")
#######################################################################################################################
# 6번
def solution(pos):
    answer = 8
    return answer

#The following is code to output testcase.
pos = "A7"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
#######################################################################################################################
# 7번
def solution(arrA, arrB):
    arrA_idx = 0
    arrB_idx = 0
    arrA_len = len(arrA)
    arrB_len = len(arrB)
    answer = []
    while arrA_idx <= (arrA_len - 1) and arrB_idx <= (arrB_len - 1):
        if arrA[arrA_idx] < arrB[arrB_idx]:
            answer.append(arrA[arrA_idx])
            arrA_idx += 1
        else:
            answer.append(arrB[arrB_idx])
            arrB_idx += 1
    while arrA_idx <= arrA_len - 1:
        answer.append(arrA[arrA_idx])
        arrA_idx += 1
    while arrB_idx <= arrB_len - 1:
        answer.append(arrB[arrB_idx])
        arrB_idx += 1
    return answer


#The following is code to output testcase.
arrA = [-2, 3, 5, 9]
arrB = [0, 1, 5]
ret = solution(arrA, arrB);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")
#######################################################################################################################
# 8번
def solution(N, votes):
    vote_counter = [0 for i in range(N + 1)]
    for i in votes:
        vote_counter[i] += 1

    max_val = max(vote_counter)

    answer = []
    for idx in range(1, N + 1):
        if vote_counter[idx] == max_val:
            answer.append(idx)
    return answer


# The following is code to output testcase. The code below is correct and you shall correct solution function.
N1 = 5
votes1 = [1, 5, 4, 3, 2, 5, 2, 5, 5, 4]
ret1 = solution(N1, votes1)

# Press Run button to receive output.
print("Solution: return value of the function is ", ret1, " .")

N2 = 4
votes2 = [1, 3, 2, 3, 2]
ret2 = solution(N2, votes2)

# Press Run button to receive output.
print("Solution: return value of the function is ", ret2, " .")
#######################################################################################################################
# 9번
def func(record):
    if record == 0:
        return 1
    elif record == 1:
        return 2
    return 0

def solution(recordA, recordB):
    cnt = 0
    for i in range(len(recordA)):
        if recordA[i] == recordB[i]:
            continue
        elif recordA[i] == func(recordB[i]):
            cnt = cnt + 3
        elif recordA[i] != func(recordB[i]) and cnt != 0:
            cnt = cnt - 1
    return cnt

#The following is code to output testcase. The code below is correct and you shall correct solution function.
recordA = [2,0,0,0,0,0,1,1,0,0]
recordB = [0,0,0,0,2,2,0,2,2,2]
ret = solution(recordA, recordB)


#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
#######################################################################################################################
# 10번
def solution(prices):
    INF = 1000000001;
    tmp = INF
    answer = -INF
    for price in prices:
        if tmp != INF:
            answer = max(answer, price - tmp)
        tmp = min(tmp, price)
    return answer


# The following is code to output testcase. The code below is correct and you shall correct solution function.
prices1 = [1, 2, 3];
ret1 = solution(prices1);

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

prices2 = [3, 1];
ret2 = solution(prices2);

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")