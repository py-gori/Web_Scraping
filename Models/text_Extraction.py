# coding=utf-8
from bs4 import BeautifulSoup
import requests

def extract(link):
    # htmlソースを取得
    res = requests.get(link)

    # BeautifulSoupの初期化
    soup = BeautifulSoup(res.text, 'html.parser')

    ## entry-listクラス(各記事単位)をentry_listに格納
    entry_list = soup.find_all(class_='entry-content')
    