from bs4 import BeautifulSoup
from datetime import datetime
import requests

def get_contents(url, day=1):
    """
    :param url: URL to scrape
           day: content uploaded day
    :return: Article name and URL of each article in dict
             {Article name: URL}
    """
    # datetime → strftime(記事リンクに含まれる日付形式に合わせる)
    day = day.strftime('%y/%m/%d')

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
            # アップロード日が指定のdayである記事のみ抽出
            if day in sub_class['href']:
                key = sub_class.h2.text.strip()
                link = sub_class['href']
                contents[key] = link
        except AttributeError:
            pass
    return contents
