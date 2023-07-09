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
WS_URL='wss://misskey.io/streaming?i='+TOKEN
print("login ended")
random.seed(hashlib.md5("こんにちは。マジで楽しみ！".encode()).hexdigest())

async def runner():
 async with websockets.connect(WS_URL) as ws:
  await ws.send(json.dumps({
   "type": "connect",
   "body": {
     "channel": "main",
     "id": "test"
   }
  }))

  while True:
   data = json.loads(await ws.recv())
   print(data)
   if data['type'] == 'channel':
    if data['body']['type'] == 'mention':
     note = data['body']['body']
     try:
       await on_mention(note)
     except Exception as e:
         print(str(e))
pules = ["ぷぇ","ぷぇ","ぷぇ","ぷぇ","ぷぅ","みぃ","ぷぅ","みぃ","！","？","ぷみ","ぷぅい","～"]
jps = ["やあ！","元気？","頑張ろう！",":send_money::is_all_scam:！","考えるな、感じろ！","こんにちは！","いえい！"]
async def on_mention(note):
    if note["reply"] is not None:
        targetnote = note["reply"]
        if targetnote is not None:
            notetext = targetnote["text"]
            Mode = "ToPule"
            if len(notetext.replace("ぷぇ","").replace("ぷぅ","").replace("ぷえぇ","").replace("ぷえ","").replace("みぃ","").replace("ぷぅえ","").replace("ぷぃ","").replace("ぷぅい","").replace("ぷみ","").replace("～","").replace("~","").replace("？","").replace("?","").replace("！","").replace("!","").replace(" ","").replace("　","").replace("\n","").replace("\r","")) <= 0:
                Mode = "ToJP"
            hashedtext = hashlib.md5(notetext.encode()).hexdigest()
            random.seed(hashedtext)
            if Mode == "ToPule":
                pulecount = random.choice(range(5,15))
                text = ""
                for i in range(pulecount):
                    text += random.choice(pules)
                print("リプライ先のノートをぷぇぷぇ語に翻訳しました！\n\n"+text)
                msk.notes_create(text="リプライ先のノートをぷぇぷぇ語に翻訳しました！\n\n"+text, reply_id=note["id"])
            elif Mode == "ToJP":
                pulecount = random.choice(range(1,5))
                text = ""
                for i in range(pulecount):
                    text += random.choice(jps)
                print("リプライ先のノートを日本語に翻訳しました！\n\n"+text)
                msk.notes_create(text="リプライ先のノートを日本語に翻訳しました！\n\n"+text, reply_id=note["id"])
                pass
asyncio.get_event_loop().run_until_complete(runner())
