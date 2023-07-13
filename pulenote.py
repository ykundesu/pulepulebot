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
if len(TOKEN) > 32:
    TOKEN = TOKEN[:32]
msk = Misskey('misskey.io', i=TOKEN)
LPBTOKEN = os.environ.get("LPBTOKEN",None)
if len(LPBTOKEN) > 32:
    LPBTOKEN = LPBTOKEN[:32]
lpbtoken = Misskey('misskey.io', i=LPBTOKEN)
hansin = Misskey("misskey.io",i=os.environ.get("HANSINTOKEN",None))
MY_ID = msk.i()['id']

pules = ["ぷぇ","ぷぇ","ぷぇ","ぷぇ","ぷぅ","みぃ","ぷぅ","みぃ","！","？","ぷみ","ぷぅい","～"]
jps = ["やあ！","元気？","頑張ろう！",":send_money::is_all_scam:！","考えるな、感じろ！","こんにちは！","いえい！"]
hansins = [":334:",":hanshin:","なんでや阪神関係ないやろ！"]
pulecount = random.choice(range(5,30))
text = ""
for i in range(pulecount):
    text += random.choice(pules)
print(text)
msk.notes_create(text=text)
lpbtoken.notes_create(text=":send_money::is_all_scam:")
hansin.notes_create(text=random.choice(hansins))
