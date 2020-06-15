# coding=utf-8
from bs4 import BeautifulSoup
import requests

def get_contents(url):
    """

    :param url: URL to scrape
    :return: Article name and URL of each article in dict
             {Article name: URL}
    """
    # htmlソースを取得
    res = requests.get(url)

    # BeautifulSoupの初期化
    soup = BeautifulSoup(res.text, 'html.parser')

    # entry-listクラス(各記事単位)をentry_listに格納
    entry_list = soup.find_all(class_='entry-list')

    # contents にkey:記事名、value:記事リンクを格納
    contents = {}
    for entry in entry_list:
        sub_class = entry.find(class_='summary')
        try:
            key = sub_class.h2.text.strip()
            link = sub_class['href']
            contents[key] = link
        except AttributeError:
            pass
    return contents
