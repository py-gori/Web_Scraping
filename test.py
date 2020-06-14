# coding=utf-8
from bs4 import BeautifulSoup
import requests

with open('osdn.txt', 'r', encoding='ISO-8859-1', newline='') as file:
    data = file.read()

# url = 'https://www.atmarkit.co.jp/ait/subtop/cloud.html'
# url = 'https://mag.osdn.jp/'
# res = requests.get(url)
# res.encoding = 'shift_jis'
# soup = BeautifulSoup(res.text, 'html.parser') # BeautifulSoupの初期化

data = data.encode('ISO-8859-1')
soup = BeautifulSoup(data, 'html.parser')

col = soup.find_all(class_='entry-list')

cols = {}
for c in col:
    sub_class = c.find(class_='summary')
    try:
        key = sub_class.h2.text.strip()
        link = sub_class['href']
        cols[key] = link
    except AttributeError:
        pass
# for key, value in cols.items():
#     print(key)
#     url = value
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     print(soup.prettify())
#     break

with open('news.txt', 'r', encoding='ISO-8859-1', newline='') as file:
    data = file.read()

data = data.encode('ISO-8859-1')
soup = BeautifulSoup(data, 'html.parser')

content = soup.find_all('p')

for c in content:
    print(c.text)