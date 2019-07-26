import csv
import requests
import bs4

url  = 'https://www.bithumb.com/'
html = requests.get(url).text
soup = bs4.BeautifulSoup(html,'html.parser')
names = soup.select('#tableAsset tbody tr td p a strong')
prices = soup.select('.sort_real')

ns = list(map(lambda x: x.text,names))
ps = list(map(lambda x: x.text,prices))


bts = []

for i in range(len(names)):
    ns[i] = ns[i].replace(' ','').replace('NEW','')
    ps[i] = float(ps[i].replace('원','').replace(',',''))
    bts.append([ns[i],ps[i]])

with open('coin_info.csv', 'w' , encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    for bt in bts :
        csv_writer.writerow(bt)


