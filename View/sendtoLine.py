# coding=utf-8

import requests

LINE_URL = 'https://notify-api.line.me/api/notify'
TOKEN = ''
HEADERS = {'Authorization': 'Bearer' + TOKEN}

message = ''
image = ''
payload = {'message': message}
file = {'imageFile': open(image, 'rb')}
r = requests.post(LINE_URL, headers=HEADERS, params=payload, files=file)