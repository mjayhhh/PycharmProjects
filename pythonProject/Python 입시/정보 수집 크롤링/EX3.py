from bs4 import BeautifulSoup as bs
import urllib.request as ur
import urllib

# 신촌 날씨 온도 출력하기
주소 = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%8B%A0%EC%B4%8C+%EB%82%A0%EC%94%A8&oquery=%EC%8B%A0%EC%B4%8C+%EB%82%A0%EC%94%A8&tqi=h7clNsp0JXVss5sZtjNssssssCh-327642'
웹문서 = ur.urlopen( 주소 )
soup = bs(웹문서.read(), 'html.parser')
온도 = soup.find_all('span' , {"class":"todaytemp"})
print("현재 신촌의 날씨는 :", 온도[0].text, "도 입니다")

# 미세먼지 출력하기
주소 = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%8B%A0%EC%B4%8C+%EB%82%A0%EC%94%A8&oquery=%EC%8B%A0%EC%B4%8C+%EB%82%A0%EC%94%A8&tqi=h7clNsp0JXVss5sZtjNssssssCh-327642'
웹문서 = ur.urlopen( 주소 )
soup = bs(웹문서.read(), 'html.parser')
미세먼지 = soup.find_all('dd', {"class": "lv1"})
print("현재 신촌의 미세먼지 농도는 :", 미세먼지[0].text ,"입니다")

# 오존 지수 출력하기
주소 = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%8B%A0%EC%B4%8C+%EB%82%A0%EC%94%A8&oquery=%EC%8B%A0%EC%B4%8C+%EB%82%A0%EC%94%A8&tqi=h7clNsp0JXVss5sZtjNssssssCh-327642'
웹문서 = ur.urlopen( 주소 )
soup = bs(웹문서.read(), 'html.parser')
미세먼지 = soup.find_all('dd', {"class": "lv2"})
print("현재 신촌의 미세먼지 농도는 :", 미세먼지[0].text ,"입니다")

# 날씨를 확인할 지역의 날씨 입력받고 출력하기
지역 = input("지역 : ")
검색어 = urllib.parse.quote( 지역 + '+ 날씨')
url = 'https://search.naver.com/search.naver?query=' + 검색어
웹문서 = ur.urlopen( url )
soup = bs(웹문서.read(), 'html.parser')
온도 = soup.find_all('span' , {"class":"todaytemp"})
print("현재", 지역 ,"의 날씨는 :", 온도[0].text, "도 입니다")