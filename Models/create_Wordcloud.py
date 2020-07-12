import os
from wordcloud.wordcloud import WordCloud

DIRPATH = ''


class WordCloudCreate(object):
    def __init__(self):
        self.background_color = 'white'
        self.fontpath = 'C://Windows//Fonts//BIZ-UDMinchoM.ttc'
        self.width = 800
        self.height = 600
        self.dir = self.get_dir()

        if not os.path.isdir(self.dir):
            os.makedirs(self.dir)

    def create(self, text, file):
        wordcloud = WordCloud(background_color=self.background_color, font_path=self.fontpath,
                              width=self.width, height=self.height).generate(text)
        filepath = os.path.join(self.dir, file)
        wordcloud.to_file(filepath)

    def get_dir(self):
        dirpath = None
        try:
            from Settings import settings
            if settings.PICTURE_DIR:
                dirpath = settings.PICTURE_DIR
        except ImportError:
            pass

        if not dirpath:
            dirpath = DIRPATH

        return dirpath