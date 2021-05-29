# 자동차 모델명을 입력을 받아 출시가를 크롤링 하기
from bs4 import BeautifulSoup as bs  # html 읽는 메소드
import urllib.request as ur  # 파이썬에 html 열기 => urlopen
import urllib

# 무한 반복
while True :

    # 입력받기
    자동차 = input("자동차의 이름 : ")
    검색어 = urllib.parse.quote(자동차)

    # 정보가 들어있는 주소 저장하기
    url = 'https://search.naver.com/search.naver?query=' + 검색어

    웹문서 = ur.urlopen( url )
    soup = bs(웹문서.read(), 'html.parser')
    # span에 값을 하나하나 넣어가지고 반복
    for i in soup.find_all("span" , {"class" : ""}):
        # 만약 뒤에 만원이라고 되있으면 저장하기
        if "만원" in i.text :
            가격 = i.text

    # 출력하기
    print("선택한 자동차의 가격 :", 가격)