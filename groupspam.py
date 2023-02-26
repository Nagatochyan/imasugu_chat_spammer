import requests
import uuid
import random
import string
import time
import json

while True:
    cookie = {'SES1': '',
              '_gai':''} #SES1と_gaiにはクッキーの値を入れる
    id = random.choices(string.ascii_letters + string.digits, k=32)
    ids = random.choices(string.ascii_letters + string.digits, k=5)
    ds = random.choices(string.ascii_letters + string.digits, k=7)
    idss = random.choices(string.ascii_letters + string.digits, k=9)
    payload = {"chat_data":"成海瑠奈「ごめんね、ぴ...(笑)」 もこう「そ、そんな、瑠奈ちゃん、どうして....」 実業家「うるさいなあ、もう消えなよ」ｶﾁｬ もこう「！」 ﾋﾞﾘﾋﾞﾘ‼︎ﾄﾞｯｶｰﾝ!!⚡️⚡️ 実業家「うびびび」（拳銃に落ちた雷から感電） 池田大作「南無妙法蓮華経！もこうくん！無事か！」 もこう「先生！」"+str(uuid.uuid4())
}

    r = requests.post("https://imasugu.web-arena.com/comet.html?mode=add",data=payload, cookies=cookie)
