from bs4 import BeautifulSoup
import requests

url = "https://dev.classmethod.jp/cloud/aws/aws-nw-architectures-net320/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
contents = soup.find('div', class_='content')
# print(contents.get_text())

# p要素の抽出
texts_p = [c.get_text() for c in contents.find_all('p')]

import re
texts_p = [t.replace('\n', '') for t in texts_p if re.match('\S', t)]

from bs4.element import Tag, NavigableString


def parse_li(li):
    buffer = []
    for child in li:
        if type(child) == NavigableString:
            buffer.append(child.string)
            pass
        elif type(child) == Tag:
            if child.find_all('li') == []:
                buffer.append(child.get_text())


texts_li = [parse_li(li) for li in contents.find_all('li')]
texts_li = [t.replace('\n', '') for t in texts_li if re.match('\S', t)]

