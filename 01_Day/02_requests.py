import requests
import bs4 #beautiful Souppy

url = 'https://finance.naver.com/sise/'

response = requests.get(url)

html = response.text #.text 요청받은 결과값에서 글자만 뽑아줘(str형식으로)


soup = bs4.BeautifulSoup(html, 'html.parser')
kospi = soup.select_one('#KOSPI_now').text # id 값은 #으로시작
print(kospi) 