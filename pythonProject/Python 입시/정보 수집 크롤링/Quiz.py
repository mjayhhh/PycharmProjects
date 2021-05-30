

# 현재 은 가격 크롤링
from bs4 import BeautifulSoup as bs
import urllib.request as ur
import urllib

url = 'https://finance.naver.com/marketindex/worldGoldDetail.nhn?marketindexCd=CMDT_GC&fdtc='
웹문서 = ur.urlopen( url )
soup = bs(웹문서.read(), 'html.parser')
가격 = soup.find_all('td')
print("현재 은 가격 :", 가격[4].text,)