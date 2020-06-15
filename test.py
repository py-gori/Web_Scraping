# coding=utf-8
from bs4 import BeautifulSoup
import requests

from datetime import datetime

now = datetime.now().strftime('%Y%m%d')
exit()

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
entry_list = [i.get_text('p') for i in soup.find_all(class_='entry-content')]
entry_list2 = soup.find_all('p')
entry_list3 = [entry_text.text.strip() for entry_text in entry_list2 if not re.match('\S', entry_text.text)]

# entry_list3 = []
# for i in entry_list2:
#     if not re.match('\S', i.text):
#         entry_list3.append(i.text.strip())
# for i in entry_list3:
#     print(i)

from janome.tokenizer import Tokenizer
t = Tokenizer()

word_list = []
for line in entry_list3:
    tokens = t.tokenize(line)
    for token in tokens:
        word = token.surface
        ps = token.part_of_speech
        if ps.find("名詞") < 0: continue
        # if word in ["<", ">", ",", "pre", "|", "[", "]"]: continue
        if word is not None:
            word_list.append(word)
strings = ' '.join(word_list)
print(strings)

exit()
from wordcloud.wordcloud import WordCloud

wordcloud = WordCloud(background_color="white",
    font_path="C:\Windows\Fonts\BIZ-UDMinchoM.ttc",
    width=800,height=600).generate(word)

wordcloud.to_file("./wordcloud_test.png")

exit()

# for i in entry_list:
#     line = i.text
#     if re.match("\S", line):
#         line.replace('\n', '')
#     else:
#         print(line.strip())
#         break

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

