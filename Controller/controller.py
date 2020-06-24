# coding=utf-8
import os
import sys
from datetime import datetime, timedelta

today = datetime.now().strftime('%Y%m%d')
uploadday = datetime.now() - timedelta(days=1)  # 記事がアップロードされた日を指定(記事リンクに含まれる日付より特定)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from Models import get_OSDN_Contents, text_Extraction, create_Wordcloud, sendtoLine
from Settings import settings

# サイトURL
URL = settings.SITE_URL

"""メイン処理"""
# サイトのコンテンツを取得
if URL == 'https://mag.osdn.jp/':
    # OSDNMagazineサイト
    contents = get_OSDN_Contents.get_contents(URL, uploadday)

if not contents:
    # コンテンツが1件も無ければ終了
    exit()

for subject, link in contents.items():
    text = text_Extraction.text_extraction(link)
    wordcloud_data = text_Extraction.janome_analysis(text)

    picturename = today + '_' + subject[0:10] + '.png'
    wordcloud = create_Wordcloud.WordCloudCreate()
    wordcloud.create(wordcloud_data, picturename)

    LINE_bot = sendtoLine.LINEBot()
    message = subject + '\n' + link
    dir = settings.PICTURE_DIR
    picture = os.path.join(dir, picturename)
    LINE_bot.send(message, picture)
