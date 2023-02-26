import requests
import uuid
import random
import string
import time
import json

while True:
    id = random.choices(string.ascii_letters + string.digits, k=20)
    ids = random.choices(string.ascii_letters + string.digits, k=5)
    payload = {"nickname": "はりーシ　"+str(uuid.uuid4()),
               "comment":"イライラしたので宣伝しますどうもはりーしです。@Halli_4 ←ツイッターのフォロワーが11万人いる超有名配信者だ。いつもvaloでトロール配信しています。みてください。"+str(id) ,
               "data_submit":"投稿" }

    r = requests.post("https://imasugu.web-arena.com/message.html",data=payload)
