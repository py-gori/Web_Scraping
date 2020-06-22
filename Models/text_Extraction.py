from bs4 import BeautifulSoup
import re
import requests


def text_extraction(link):
    """
    :param link: The page you want to display
    :return:
    """
    # htmlソースを取得
    res = requests.get(link)

    # BeautifulSoupの初期化
    soup = BeautifulSoup(res.text, 'html.parser')

    # <p>タグ(本文)をentry_textに格納
    entry_text = soup.find_all('p')

    # entry_textからテキスト情報のみ抽出
    text = [line.text.strip() for line in entry_text if not re.match('\S', line.text)]
    return text


def janome_analysis(text):
    from janome.tokenizer import Tokenizer
    t = Tokenizer()

    word_list = []
    for line in text:
        tokens = t.tokenize(line)
        for token in tokens:
            word = token.surface
            ps = token.part_of_speech
            if ps.find('名詞') < 0:
                continue
            # if word in ["<", ">", ",", "pre", "|", "[", "]"]: continue
            if word is not None:
                word_list.append(word)
    wordcloud_data = ' '.join(word_list)
    return wordcloud_data
