# coding=utf-8
import os
import sys
from datetime import datetime

today = datetime.now().strftime('%Y%m%d')
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from Models import get_OSDN_Contents, text_Extraction, create_Wordcloud

# OSDN.magazinサイトURL
URL = 'https://mag.osdn.jp/'

"""メイン処理"""
# OSDNmagazineサイトのコンテンツを取得
contents = get_OSDN_Contents.get_contents(URL)
# content = [text_Extraction.text_extraction(link) for subject, link in contents.items()]

for subject, link in contents.items():
    text = text_Extraction.text_extraction(link)
    word_clouddata = text_Extraction.janome_analysis(text)

    output_picturename = subject[0:10] + '_' + today
    create_Wordcloud.create_wordcloud(word_clouddata, output_picturename)
