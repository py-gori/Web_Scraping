from wordcloud.wordcloud import WordCloud
text_file = open("tukikage_2.txt", encoding="utf-8")
bindata = text_file.read()
txt = bindata

wordcloud = WordCloud(background_color="white",
    font_path="C:\Windows\Fonts\BIZ-UDMinchoM.ttc",
    width=800,height=600).generate(txt)

wordcloud.to_file("./wordcloud_tukikage.png")


def morpheme_analysis(self):
    logger.info('学習データ整形処理を開始します。%s', __file__)
    tickets_description = file.load_file('tickets_description.csv')
    t = Tokenizer()
    words_list = []
    for ticket_description in tickets_description:
        noun_list = []
        for line in ticket_description:
            tokens = t.tokenize(line)
            for token in tokens:
                word = token.surface
                ps = token.part_of_speech
                # 名詞以外もしくは、数字ならば除外
                if ps.find('名詞') < 0 or ps.find('数') > 0:
                    continue
                #                if word in ["(", ")", "<", ">", ",", "/", "pre", "|", "[", "]"]:
                #                    continue
                #                p = re.compile('[0-9]{0,10}')
                #                if p.fullmatch(word) is not None:
                #                    continue
                #                if word is not None:
                noun_list.append(word)
        ticket_nouns = ' '.join(noun_list)
        words_list.append(ticket_nouns)
    logger.info('学習データ整形処理を終了します。%s', __file__)
    return words_list
