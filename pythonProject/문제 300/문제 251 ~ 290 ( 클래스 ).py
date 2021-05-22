# 251. 클래스, 객체, 인스턴스에 대해 설명해보세요
# 간단하게 클래스   : 틀
#         객체     : 데이터
#         인스턴스 : 결과물

# 252. 비어있는 사람 (Human) 클래스를 "정의" 해보세요
class Human :
    pass

# 253. 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요
class Human :
    print("응애응애")

areum = Human

# 254. 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요
class Human() :
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

areum = Human("아름", 25, "여자")

# 256. 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요.
print(areum.age)
print(areum.name)
print(areum.gender)

# 257. 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.
class Human() :
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print(self.name)
        print(self.gender)
        print(self.age)

areum = Human("아름", 25, "여자")
areum.who()

# 258. 사람 (Huamn) 클래스에서 이름, 나이, 성별을 받는 selfInfo 메소드를 추가하세요.
class Human() :
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def selfInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print(self.name)
        print(self.gender)
        print(self.age)

areum = Human("모름",0,"모름")
areum.selfInfo("아름", 25, "여자")

# 259. 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요
class Human() :
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def selfInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print(self.name)
        print(self.gender)
        print(self.age)

    def __del__(self):
        print("나의 죽음을 알리지 말라")

areum = Human("아름", 25, "여자")
del areum

# 260. 아래와 같은 에러가 발생한 원인에 대해 설명하세요.
# class OMG :
#     def print() :
#         print("Oh my god")
#
# myStock = OMG()
# myStock.print()

# 함수를 만들 때 self든 뭐든 자기 자신을 가리키는 것을 넣어야 하는데 넣지 않아서

# 261. 주식 종목에 대한 정보를 저장하는 Stock 클래스를 정의해보세요
class Stock :
    pass

# 262. Stock 클래스의 객체가 생성될 때 종목명과 종목 코드를 입력받을 수 있는 생성자를 정의해 보세요
class Stock :
    def __init__(self, name, code):
        self.name = name
        self.code = code

삼성 = Stock("삼성전자", "005930")

# 263. 객체에 종목명을 입력할 수 있는 set_name 메소드를 추가해보세요
class Stock :
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

a = Stock(None, None)
a.set_name("삼성전자")

# 264. 객체에 종목 코드를 입력할 수 있는 set_code 메소드를 추가해보세요
class Stock :
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

a = Stock(None, None)
a.set_name("삼성전자")
a.set_code("005930")

# 265. 종목명과 종코드를 리턴하는 get_name, get_code 메소드를 추가하세요.
class Stock :
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_code(self):
        print(self.code)

    def get_name(self):
        print(self.name)

a = Stock(None, None)
a.set_name("삼성전자")
a.set_code("005930")
a.get_code()
a.get_name()

# 266. 생성자에서 종목명, 종목콛, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요. PER,PBR, 배당수익률은 float 타입입니다.
class Stock :
    def __init__(self, name, code, PER, PBR, 배당수익률):
        self.PER = PER
        self.PBR = PBR
        self.배당수익률 = 배당수익률
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_code(self):
        print(self.code)

    def get_name(self):
        print(self.name)

# 267. 266번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요


# 268. PER, PBR, 배당 수익률은 변경될 수 있는 값입니다. 이 값을 변경할 때 사용하는 메소드를 추가하세요
class Stock :
    def __init__(self, name, code, PER, PBR, 배당수익률):
        self.PER = PER
        self.PBR = PBR
        self.배당수익률 = 배당수익률
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_code(self):
        print(self.code)

    def get_name(self):
        print(self.name)

    def set_PER(self, PER):
        self.PER = PER

    def set_PBR(self, PBR):
        self.PBR = PBR

    def set_배당수익률(self, 배당수익률):
        self.배당수익률 = 배당수익률

# 269. 267번에서 생성한 객체에 set_per 메소드를 호출하여 per 값을 12.75로 수정해보세요
삼성 = Stock("삼성", "005930" , 15.79, 1.33, 2.83)
삼성.set_PER(12.75)

# 270. 아래 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장하세요
삼성전자 = Stock("삼성전자","005930",15.79,1.33,2.83)
현대차 = Stock("현대차","005380",8.70,0.35,4.27)
LG전자 = Stock("LG전자","066570",317.34,0.69,1.37)
종목 = []
종목.append(삼성전자)
종목.append(현대차)
종목.append(LG전자)

# 271. 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. Account 클래스를 생성한 후 생성자를
# 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다. 은행이름은 SC은행으로 계좌 번호는 3자리-2자리-6
# 자리 형태로 랜덤하게 생성됩니다.
import random
class Account :
    def __init__(self, money):
        self.name = "SC은행"
        self.person = "파이썬"
        self.money = money
        self.number = str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + "-" + str(random.randint(1,9)) + str(random.randint(1,9)) + "-" + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9))

계좌 = Account(10000)
print(계좌.number)

# 272. 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요
class Account :
    def __init__(self, money, value=0):
        self.counter = value + 1
        self.name = "SC은행"
        self.person = "파이썬"
        self.money = money
        self.number = str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + "-" + str(random.randint(1,9)) + str(random.randint(1,9)) + "-" + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9))
    def number_of_counters(self):
        return self.counter

계좌 = Account(10000)
number = 계좌.number_of_counters()

# 273. Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메소드를 추가하세요.
class Account :
    def __init__(self, money, value=0):
        self.counter = value + 1
        self.name = "SC은행"
        self.person = "파이썬"
        self.money = money
        self.number = str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + "-" + str(random.randint(1,9)) + str(random.randint(1,9)) + "-" + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9))
    def get_account_num(self):
        return self.counter

# 275. Account 클래스에 입금을 위한 deposit 메소드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.
class Account :
    def __init__(self, money, value=0):
        self.counter = value + 1
        self.name = "SC은행"
        self.money = money
        self.person = "파이썬"
        self.number = str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + "-" + str(random.randint(1,9)) + str(random.randint(1,9)) + "-" + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9))
    def get_account_num(self):
        return self.counter

    def deposit(self, money):
        if money < 1:
            print("최소 1원 이상만 가능합니다")
        else:
            self.money += money
            print("입금이 완료 되었습니다.")

# 274. Account 클래스에 출금을 위한 withdraw 메소드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다
class Account :
    def __init__(self, money, value=0):
        self.counter = value + 1
        self.name = "SC은행"
        self.money = money
        self.person = "파이썬"
        self.number = str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + "-" + str(random.randint(1,9)) + str(random.randint(1,9)) + "-" + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9))
    def get_account_num(self):
        return self.counter
    def deposit(self, money):
        if money < 1 :
            print("최소 1원 이상만 가능합니다")
        else :
            self.money += money
            print("입금이 완료 되었습니다.")
    def withdraw(self,money):
        if money > self.money :
            print("계좌의 잔고 이상으로 출금할 수는 없습니다")
        else :
            self.money -= money
            print("출금이 완료되었습니다")

# 276. Account 인스턴스에 저장된 정보를 출력하는 display_info() 메소드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하
# 세요.
class Account :
    def __init__(self, money, value=0):
        self.counter = value + 1
        self.name = "SC은행"
        self.person = "파이썬"
        self.money = money
        self.number = str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + "-" + str(random.randint(1,9)) + str(random.randint(1,9)) + "-" + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9))

    def get_account_num(self):
        return self.counter

    def deposit(self, money):
        if money < 1 :
            print("최소 1원 이상만 가능합니다")
        else :
            self.money += money
            print("입금이 완료 되었습니다.")

    def withdraw(self, money) :
        if money > self.money:
            print("계좌의 잔고 이상으로 출금할 수는 없습니다")
        else :
            self.money -= money
            print("출금이 완료되었습니다")

    def display_info(self):
        a = 1
        print("은행이름 :", self.name)
        print("예금주 :", self.person)
        print("계좌번호 :",self.number)
        self.money = str(self.money)
        for i in self.money:
            if a % 3 == 0:
                print(",", end='')
            print(i, end='')
            a += 1

계좌 = Account(10000)
계좌.display_info()

# 277. 입금횟수가 5회가 될 때 잔고를 기준으로 1 %의 이자가 잔고에 추가되도록 코드를 변경해보세요
class Account :
    def __init__(self, money, value=0):
        self.counter = value + 1
        self.name = "SC은행"
        self.person = "파이썬"
        self.money = money
        self.number = str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + "-" + str(random.randint(1,9)) + str(random.randint(1,9)) + "-" + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9))

    def get_account_num(self):
        return self.counter

    def deposit(self, money, value = 0):
        if money < 1 :
            print("최소 1원 이상만 가능합니다")
        else :
            self.money += money
            print("입금이 완료 되었습니다.")
            if self.counter2 % 5 == 0 :
                self.money += self.money * (1 / 100)
            self.counter2 = value + 1

    def withdraw(self, money) :
        if money > self.money:
            print("계좌의 잔고 이상으로 출금할 수는 없습니다")
        else :
            self.money -= money
            print("출금이 완료되었습니다")

    def display_info(self):
        a = 1
        print("은행이름 :", self.name)
        print("예금주 :", self.person)
        print("계좌번호 :",self.number)
        self.money = str(self.money)
        for i in self.money:
            if a % 3 == 0:
                print(",", end='')
            print(i, end='')
            a += 1
