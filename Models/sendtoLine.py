import requests


class LINEBot(object):
    def __init__(self):
        self.url = None
        self.token = None

        try:
            from Settings import settings
            self.url = settings.LINE_URL
            self.token = settings.TOKEN
        except ImportError as ie:
            print('ImportError:', ie)

        self.headers = {'Authorization': 'Bearer ' + self.token}

    def send(self, message=None, image=None):
        file = {}
        if image:
            file = {'imageFile': open(image, 'rb')}

        payload = {'message': message}
        r = requests.post(self.url, headers=self.headers, params=payload, files=file)
