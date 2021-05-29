# 크롤링 : 인터넷에서 데이터 추출하기
from bs4 import BeautifulSoup as bs
import urllib.request as ur

# 1. 인터넷 주소 넣기
url = 'http://quotes.toscrape.com/'
# 2. 인터넷 주소 파이썬으로 가져오기
html = ur.urlopen(url)

# 3. read() : 읽기 함수, 인터넷을 읽어오기
soup = bs(html.read(), 'html.parser')

# 4. 읽어온것 중 찾기( 'span' ) 을 찾아서  첫번째 텍스트를 가져오기
print( soup.find_all('span')[0].text)
# 마크업언어[html]에서 'span' 태그를 찾아서 태그 사이에 있는 텍스트 가져오기

# 5. 일거온 것 중 ('span')을 찾고 그 텍스트 중 2번째와 4번째 텍스트를 출력하기
print( soup.find_all('span')[2].text)
print( soup.find_all('span')[4].text)

# 'span'을 찾아 그 값을 i에 넣고 i의 텍스트를 출력
for i in soup.find_all('span'):
    print(i.text)

# span에 포함된 해당 클래스만 찾기
for i in soup.find_all('div', {"class" : "quote"}):
    print(i.text)