import urllib.request
import json
import re

# 데이터 검색 코드
def 네이버검색( 카테고리 ) :
    클라이언트id = "EHAD3_qMeYxT10CFrFSW"
    클라이언트secret = "vPIci1a8No"
    url = "https://openapi.naver.com/v1/search/" + 카테고리 + ".json"  # json 결과
    option = "&display=1sort=count" # display : 출력 개수 : 검색결과 수
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
            print("이름 : " + 타이틀)
            if 카테고리 == "shop":
                제조사명 = re.sub('<.+?>', "", i['maker'], 0, re.I | re.S)
                print("제조사명 : " + 제조사명)
                브랜드명 = re.sub('<.+?>', "", i['brand'], 0, re.I | re.S)
                print("브랜드명 : " + 브랜드명)
            if 카테고리 == "book":
                저자명 = re.sub('<.+?>', "", i['author'], 0, re.I | re.S)
                print("저자명 : " + 저자명)
                출판사 = re.sub('<.+?>', "", i['publisher'], 0, re.I | re.S)
                print("출판사 : " + 출판사)
            if 카테고리 == "movie":
                평점 = re.sub('<.+?>', "", i['userRating'], 0, re.I | re.S)
                print("평점 : " + 평점)
                감독 = re.sub('<.+?>', "", i['director'], 0, re.I | re.S)
                print("감독 : " + 감독)
                출연배우 = re.sub('<.+?>', "", i['actor'], 0, re.I | re.S)
                print("출연 배우 : " + 출연배우)
    else:
        print("Error Code:" + rescode)

# 검색 프로그램 코드
while True :
    print("검색[naverAPI] 프로그램")
    print("카테고리[ 1. 영화 2. 쇼핑 3. 도서 ] 0. 종료")
    선택 = int(input("검색 : "))
    if 선택 == 1 :
        카테고리 = "movie"
        네이버검색(카테고리)
    elif 선택 == 2 :
        카테고리 = "shop"
        네이버검색(카테고리)
    elif 선택 == 3 :
        카테고리 = "book"
        네이버검색(카테고리)
    else :
        print("이용해 주셔서 감사합니다")
        break
