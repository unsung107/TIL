import requests
from bs4 import BeautifulSoup


url = 'https://www.naver.com/' #class 는 .으로접근

selector = '.ah_k'

 #class 네임 다음 띄어쓰기는 클래스 안에서 또 검색을 하겠다라는 의미
html = requests.get(url).text



soup = BeautifulSoup(html,"html.parser")


ranks = soup.select(selector) #ul.ah_l:nth-child(5) > li:nth-child(2) > a:nth-child(1) > span:nth-child(2)

for rank in ranks :
    print(rank.text)