import asyncio
import json
import websockets
from misskey import Misskey
import hashlib
import random
import os
print("library loaded")
TOKEN=os.environ.get("PULEPULETOKEN",None)
if TOKEN == None:
    print("トークンなし")
    a()
msk = Misskey('misskey.io', i=TOKEN)
MY_ID = msk.i()['id']

pules = ["ぷぇ","ぷぇ","ぷぇ","ぷぇ","ぷぅ","みぃ","ぷぅ","みぃ","！","？","ぷみ","ぷぅい","～"]
jps = ["やあ！","元気？","頑張ろう！",":send_money::is_all_scam:！","考えるな、感じろ！","こんにちは！","いえい！"]
pulecount = random.choice(range(5,30))
text = ""
for i in range(pulecount):
    text += random.choice(pules)
print(text)
msk.notes_create(text=text)