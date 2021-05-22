# 241. datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요
import datetime
now = datetime.datetime.now()
print(now)

# 242. datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요
print(type(now))

# 243. datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요
print(datetime.datetime.now() - datetime.timedelta(days=5))
print(datetime.datetime.now() - datetime.timedelta(days=4))
print(datetime.datetime.now() - datetime.timedelta(days=3))
print(datetime.datetime.now() - datetime.timedelta(days=2))
print(datetime.datetime.now() - datetime.timedelta(days=1))

# 244. 현재 시간을 얻어온 후 다음과 같은 포맷으로 시간으로 출력해보세요. strftime 메서드를 사용하세요
print(now.strftime('%H:%M:%S'))

# 245. datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만드어
# 줍니다. "2020-05-04"의 문자열을 시간 타입으로 변환해보세요
time = datetime.datetime.strptime("2020-05-04", "%Y-%m-%d")
print(time)
print(type(time))

# # 246. time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요
import time
import datetime
while True :
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)

# 247. 모듈을 임포트 하는 4가지 방식에 대해 설명해보세요
# import 이름
# import 이름 as 이름
# from 이름 import 이름
# from 이름 import *

# 248. os 모듈의 gatcwd 함수를 호출하여 현재 디레곹리의 경로를 화면에 출력해보세요
import os
path = os.getcwd()
print(path)

# 249. 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요
import os
os.rename('C:\\Users\\User\\Desktop\\아무거나2', 'C:\\Users\\User\\Desktop\\아무거나')

# 250. numpy 모듈의 arange 함수를 사용해서 0.0부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.
import numpy
print(numpy.arange(0.0, 5.1, 0.1))


