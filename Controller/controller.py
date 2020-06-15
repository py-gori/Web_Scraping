# coding=utf-8
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from Models import get_OSDN_Contents, text_Extraction

# OSDN.magazinサイトURL
URL = 'https://mag.osdn.jp/'

"""メイン処理"""
# OSDNmagazineサイトのコンテンツを取得
contents = get_OSDN_Contents.get_contents(URL)
content = [text_Extraction.extract(link) for subject, link in contents.items()]
