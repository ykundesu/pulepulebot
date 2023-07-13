import asyncio
import json
import websockets
from misskey import Misskey
import hashlib
import random
import os
print("library loaded")
def login(evname):
    token = os.environ.get(evname,None)
    if len(token) > 32:
        token = token[:32]
        print(token[0])
        print(token[31])
    print(token)
    if token == None:
        print("トークンなし:"+evname)
        a()
    return Misskey('misskey.io', i=token),token
msk, TOKEN = login("PULEPULETOKEN")
letterpack = login("LPBTOKEN")[0]
allscam = login("LASBTOKEN")[0]
hansin = login("HANSINTOKEN")[0]
MY_ID = msk.i()['id']
WS_URL='wss://misskey.io/streaming?i='+TOKEN
print("login ended")
#random.seed(hashlib.md5("こんにちは。マジで楽しみ！".encode()).hexdigest())

async def runner():
 async with websockets.connect(WS_URL) as ws:
  await ws.send(json.dumps({
   "type": "connect",
   "body": {
     "channel": "localTimeline",
     "id": "pulepulebot"
   }
  }))

  while True:
   try:
       data = json.loads(await ws.recv())
   except websockets.exceptions.ConnectionClosedError as e:
       print(str(e))
       await runner()    
       continue
   if data['type'] == 'channel':
    if data['body']['type'] == 'note':
     note = data['body']['body']
     try:
        await on_mention(note)
     except Exception as e:
         print(str(e))
pules = ["ぷぇ","ぷぇ","ぷぇ","ぷぇ","ぷぅ","みぃ","ぷぅ","みぃ","！","？","ぷみ","ぷぅい","～"]
jps = ["やあ！","元気？","頑張ろう！",":send_money::is_all_scam:！","考えるな、感じろ！","こんにちは！","いえい！"]
async def on_mention(note):
 if note.get('mentions') and MY_ID in note['mentions']:
  if note.get("reply"):
        targetnote = note["reply"]
        if targetnote is not None:
            notetext = targetnote["text"]
            Mode = "ToPule"
            if len(notetext.replace("ぷぇ","").replace("ぷえぇ","").replace("ぷえ","").replace("みぃ","").replace("ぷぅえ","").replace("ぷぃ","").replace("ぷぅい","").replace("ぷみ","").replace("～","").replace("ぷぅ","").replace("~","").replace("？","").replace("?","").replace("！","").replace("!","").replace(" ","").replace("　","").replace("\n","").replace("\r","")) <= 0:
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
                try:
                 msk.notes_create(text="リプライ先のノートを日本語に翻訳しました！\n\n"+text, reply_id=note["id"])
                except Exception as e:
                     print(str(e))
                pass
 try:
 #print(note)
  if note.get("text"):
   if ":send_money:" in note.get("text"):
     letterpack.notes_reactions_create(note.get("id"),":send_money:")
     letterpack.notes_create(renote_id=note.get("id"),visibility="home")
     print("レターパックで現金送れ")
     if ":is_all_scam:" in note.get("text"):
         allscam.notes_reactions_create(note.get("id"),":is_all_scam:")
         allscam.notes_create(renote_id=note.get("id"),visibility="home")
         print("はすべて詐欺です")
   if "334" in note.get("text").replace("-","") or "hansin" in note.get("text").replace("-",""):
     hansin.notes_reactions_create(note.get("id"),random.choice([":hanshin:",":334:"]))
     hansin.notes_create(renote_id=note.get("id"),visibility="home")
 except Exception as e:
     print(str(e))
asyncio.get_event_loop().run_until_complete(runner())
