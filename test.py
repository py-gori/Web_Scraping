# coding=utf-8
from bs4 import BeautifulSoup
import requests
"""
# with open('osdn.txt', 'r', encoding='ISO-8859-1', newline='') as file:
# data = file.read()
# url = 'https://www.atmarkit.co.jp/ait/subtop/cloud.html'
"""
## OSDN.magazinサイトURL
url = 'https://mag.osdn.jp/20/06/09/160000'

## htmlソースを取得
res = requests.get(url)

"""
# res.encoding = 'shift_jis'
"""

## BeautifulSoupの初期化
soup = BeautifulSoup(res.text, 'html.parser')

"""
# data = data.encode('ISO-8859-1')
# soup = BeautifulSoup(data, 'html.parser')

"""
import re
## entry-listクラス(各記事単位)をentry_listに格納
entry_list = soup.find_all(class_='entry-content')
for i in entry_list:
    if re.match("\S", i.text):
        print(i.text)
    # else:
        # print(i.text.strip())

exit()

for entry in entry_list.find('p'):
    print(entry.strip())

## contents にkey:記事名、value:記事リンクを格納
# contents = {}
# for entry in entry_list:
#     sub_class = entry.find(class_='summary')
#     try:
#         key = sub_class.h2.text.strip()
#         link = sub_class['href']
#         contents[key] = link
#     except AttributeError:
#         pass

