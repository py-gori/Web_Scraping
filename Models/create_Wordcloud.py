from wordcloud.wordcloud import WordCloud

background_color = 'white'
fontpath = 'C:\Windows\Fonts\BIZ-UDMinchoM.ttc'
width = 800
height = 600


def create_wordcloud(text, filename):
    wordcloud = WordCloud(background_color=background_color, font_path=fontpath, width=width,
                          height=height).generate(text)

    wordcloud.to_file('..\Picture' + filename + '.png')
