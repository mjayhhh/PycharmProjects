# 1
answer = 0
n = 7
for i in range(2019):
    n *= 7
print("1번의 값 :", n % 5, "/ 1번의 답 : 2번")


# 4
numbers = [8, 5, 4, 9, 11, 1, 12, 15, 2, 6, 7, 10]
n = 0
m = 0
n2 = 0
for _ in range(3):
    for i in range(len(numbers)):
        while n != 1 :
            if i + m + 1 < len(numbers):
                if numbers[i + m] > numbers[i + m + 1]:
                    n2 = numbers[i + m]
                    numbers[i + m] = numbers[i + m + 1]
                    numbers[i + m + 1] = n2
                    m += 1
                else :
                    n = 1
            else:
                n = 1
        m = 0
        n =0
print("4번의 값 :", numbers, "/ 4번의 답 : 4번")


# 7
n = 0
for i in range(3, 16) :
    n += i
answer = n - 106
print("7번의 값 :", answer, "/ 7번의 답 : 3번")

# 8
answer = 0
m = 1
A = 10
B = 11
C = 12
D = 13
E = 14
F = 15
G = 16
H = 17
I = 18
J = 19
n = "GD"
length = len(n)
for i in n :
    if i == "A":
        if m == length :
            answer += A
        else :
            answer += A * (2 * (10 ** (length - m)))
            m += 1
    elif i == "B":
        if m == length :
            answer += B
        else :
            answer += B * (2 * (10 ** (length - m)))
            m += 1
    elif i == "C":
        if m == length :
            answer += C
        else :
            answer += C * (2 * (10 ** (length - m)))
            m += 1
    elif i == "D":
        if m == length :
            answer += D
        else :
            answer += D * (2 * (10 ** (length - m)))
            m += 1
    elif i == "F":
        if m == length :
            answer += F
        else :
            answer += F * (2 * (10 ** (length - m)))
            m += 1
    elif i == "G":
        if m == length :
            answer += G
        else :
            answer += G * (2 * (10 ** (length - m)))
            m += 1
    elif i == "H":
        if m == length :
            answer += H
        else :
            answer += H * (2 * (10 ** (length - m)))
            m += 1
    elif i == "I":
        if m == length :
            answer += I
        else :
            answer += I * (2 * (10 ** (length - m)))
            m += 1
    elif i == "J":
        if m == length :
            answer += J
        else :
            answer += J * (2 * (10 ** (length - m)))
            m += 1
    else :
        if m == length :
            answer += A
        else :
            answer += i * (2 * (10 ** (length - m)))
            m += 1
print("8번의 값 :", answer, "/ 8번의 답 : 4번")


# 11번
list = []
for i in range(1, 3055) :
    if 12378 % i == 0 :
        if 3054 % i == 0 :
            list.append(i)
print("11번의 값 :", max(list), "/ 11번의 답 : 2번")


# 16번
num = 2 ** 2017 + 3 ** 2017 + 5 ** 2017 + 7 ** 2017
print("16번의 값 :", num % 10, "/ 16번의 답 : 4번 ")


# 19번
num = 0
count = 0
for i in range(1, 100000):
    num += i
    while num != 0 :
        if num % 10 == 1:
            count += 1
            num //= 10
        else :
            num //= 10
print("19번의 값 :", count, "/ 19번의 답 : 4번")

# 21번
num = [2, 3, 5, 7]
answer = 0
for i in num :
    answer += i ** 2017
print("21번의 값 :", answer % 10, "/ 21번의 답 : 4번")

# 22번
num = 0
answer = 0
while num < 1:
    num += 1 / 60 + 1 / 45 + 1 / 90
    answer += 1
print("22의 값 :", answer, "/ 22번의 값 : 1번")

# 28번
answer = 0
for i in range(1, 8) :
    for a in range(1, 8) :
        for n in range(1, 8) :
            for m in range(1, 8) :
                if i + a + n + m == 10 :
                    answer += 1
print("23의 값 :", answer, "/ 23번의 값 : 2번")

# 29번
answer = 0
num = 0
nums = []
for i in range(1, 10) :
    for a in range(1, 10) :
        for n in range(1, 10) :
            for m in range(1, 10) :
                nums.append(i)
                nums.append(a)
                nums.append(n)
                nums.append(m)

while True :
    n = nums[num] * 1000 + nums[num + 1] * 100 + nums[num + 2] * 10 + nums[num + 3]
    n2 = nums[num + 3] * 1000 + nums[num + 2] * 100 + nums[num + 1] * 10 + nums[num]
    for i in range(1, 10) :
        if n // 1000 == n // 100 % 10 :
            break
        elif n // 1000 == n // 10 % 10 :
            break
        elif n // 1000 == n % 10 :
            break
        elif n // 100 % 10 == n // 10 % 10 :
            break
        elif n // 100 % 10 == n % 10 :
            break
        elif n // 10 % 10 == n % 10 :
            break
        elif n * i == n2 :
            answer = nums[num + 3]
            break
    num += 1
    if answer != 0 :
        break
print("30번의 값 :", answer, "/ 30번의 답 : 4번")

# 32번
print("32번의 값 :", 7 ** 2014 % 10, "/ 32번의 답 : 5번")

# 35번
answer = 0
for i in range(1, 10) :
    for a in range(1, 10) :
        for n in range(1,10) :
            num = i * 100 + i * 10 + i + a * 100 + a * 10 + a + n * 100 + n * 10 + n
            if num == n * 1000 + a * 100 + a * 10 + i :
                answer = i + a + n
                break
print("35번의 값 :", answer, "/ 35번의 답 : 4번")

# 36번
answer = 0
m = 1
n = []
for i in range(1, 11) :
    for a in range(1, i) :
        n.append(a)
    for o in n :
        m += m * o
    answer += m
print("36번의 값 :", answer % 10, "/ 36번의 값 : 5번")

# 37번
answer = 0
for i in range(1, 101) :
    if i >= 100 :
        answer += i % 10
        answer += i // 10 % 10
        answer += i // 100
    elif i >= 10 :
        answer += i % 10
        answer += i // 10
    else :
        answer += i
print("37번의 값 :", answer, "/ 37번의 답 : 3번")

# 41번
answer = 0
num = [23, 24, 26, 31, 33]
for i in range(1, 11):
    for a in range(1, 11):
        answer += 5 * i
        answer += 7 * a
        for n in num :
            if answer == n :
                num.remove(answer)
        answer = 0

print("41번의 값 :", num, "/ 41번의 답 : 1번")

# 46
answer = 0
time = 0
while True :
    answer += 1 / 120
    answer += 1 / 180
    answer += 1 / 360
    time += 1
    if answer >= 1:
        break
print("46번의 값 :", time / 60, "/ 46번의 답 : 1번")

# 48
print("48번의 값 :", 13 ** 13 % 10, "/ 48번의 답 : 2번")

# 49
num = []
for i in range(1, 100):
    for a in range(1, 100):
        if i * a == 1000 :
            num.append(i + a)
print("49번의 값 :", min(num), "/ 49번의 답 : 2번")

# 50
answer = 0
num = 1
while True :
    if num % 2 == 1 :
        if num % 3 == 2 :
            if num % 4 == 3:
                if num % 5 == 4:
                    if num % 6 == 5 :
                        break
    num += 1
print("50번의 값 :", num % 7, "/ 50번의 답 : 3번")

# 59
answer = 0
true = []
false = []
num = [False for _ in range(101)]
for i in range(1, 101) :
    for a in range(1, 101) :
        if a % i == 0 :
            if num[a] == True :
                num[a] = False
            else :
                num[a] = True
for i in num :
    if i == True :
        true.append(i)
    else :
        false.append(i)

if len(true) > len(false) :
    answer = false
else :
    answer = true

print("59번의 값 :",answer, "/ 59번의 답 : 1")

# 69
str = ['a', 'b', 'c']
list = []
for i in range(0, 3):
    for a in range(0, 3) :
        for n in range(0, 3) :
            for m in range(0, 3) :
                for o in range(0, 3):
                    for p in range(0, 3):
                        for q in range(0, 3):
                            for s in range(0, 3) :
                                for e in range(0, 3):
                                    list.append(str[i] + str[a] + str[n] + str[m] + str[o] + str[p] + str[q] + str[s]  + str[e])
answer = []
for i in list :
    if i[0] == i[8] :
        if i[1] == i[7] :
            if i[2] == i[6] :
                if i[3] == i[5] :
                    answer.append(i)
print("69번의 값 :", answer[199] ,"/ 69번의 답 : 2번")

# 78
num1 = []
num2 = []
num = []
for i in range(100, 1000) :
    num.append(i)
for i in num :
    for a in range(1, 10) :
        num1.append(i * a)

for i in range(10, 100) :
    for a in range(10, 100):
        num2.append(i * a)


