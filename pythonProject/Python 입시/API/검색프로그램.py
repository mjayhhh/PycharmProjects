# 네이버 검색 API를 이용한 Json 가공 프로그램
    # JSON : 키-값 = > 한 쌍 <---- 딕셔너리와 유사

import urllib.request
import json
import re

# 데이터 검색 코드
def 네이버검색( 카테고리, 검색결과수) :

    클라이언트id = "EHAD3_qMeYxT10CFrFSW"
    클라이언트secret = "vPIci1a8No"
    url = "https://openapi.naver.com/v1/search/" + 카테고리 + ".json"  # json 결과
    option = "&display="+검색결과수+"sort=count" # display : 출력 개수 : 검색결과 수
    query = "?query=" + urllib.parse.quote(input("검색 정보 입력 : "))
    url_query = url+query+option

    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id", 클라이언트id)
    request.add_header("X-Naver-Client-Secret", 클라이언트secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        검색결과 = response_body.decode('utf-8')  # utf-8 : 한글 지원

        # 검색 결과 가공 하기
        json결과 = json.loads(검색결과)

        결과리스트 = []
        for i in json결과['items']:
            타이틀 = re.sub('<.+?>', "", i['title'], 0, re.I | re.S)
            print(타이틀)
            if 카테고리 == "shop":
                가격 = re.sub('<.+?>', "", i['lprice'], 0, re.I | re.S)
                print(가격)
            if 카테고리 == "movie":
                평점 = re.sub('<.+?>', "", i['userRating'], 0, re.I | re.S)
                print(평점)
            if 카테고리 == "news":
                내용 = re.sub('<.+?>', "", i['description'], 0, re.I | re.S)
                print(내용)


    else:
        print("Error Code:" + rescode)


# 검색 프로그램 코드
while True :
    print("검색[naverAPI] 프로그램")
    print("카테고리[ 1. 뉴스 2. 쇼핑 3. 도서 4. 영화 5. 사전 6. 지역] 0. 종료")
    선택 = int(input("검색 : "))
    if 선택 == 1 :
        카테고리 = "news"
        검색결과수 = input("몇개를 출력할까요? ")
        네이버검색(카테고리, 검색결과수)
    elif 선택 == 2 :
        카테고리 = "shop"
        검색결과수 = input("몇개를 출력할까요? ")
        네이버검색(카테고리, 검색결과수)
    elif 선택 == 3 :
        카테고리 = "book"
        검색결과수 = input("몇개를 출력할까요? ")
        네이버검색(카테고리, 검색결과수)
    elif 선택 == 4 :
        카테고리 = "movie"
        검색결과수 = input("몇개를 출력할까요? ")
        네이버검색(카테고리, 검색결과수)
    elif 선택 == 5 :
        카테고리 = "encyc"
        검색결과수 = input("몇개를 출력할까요? ")
        네이버검색(카테고리, 검색결과수)
    elif 선택 == 6 :
        카테고리 = "local"
        검색결과수 = input("몇개를 출력할까요? ")
        네이버검색(카테고리, 검색결과수)
    else :
        print("이용해 주셔서 감사합니다")
        break # 반복문 탈출
