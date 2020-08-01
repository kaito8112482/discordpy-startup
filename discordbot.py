import urllib.request

def download():
    url = 'https://services9.arcgis.com/XenOZPW9k4gDSO12/arcgis/rest/services/COVID19_JapanCaseData/FeatureServer/0/query?where=%E9%80%9A%E3%81%97%3E-1&returnIdsOnly=false&returnCountOnly=false&&f=pgeojson&outFields=*&orderByFields=%E9%80%9A%E3%81%97'
    title = 'COVID-19_data.json'
    urllib.request.urlretrieve(url, "{0}".format(title))
    
    
    import download
import json
from collections import defaultdict
import discord

TOKEN = 'corona'
CHANNEK_ID = '739097587767836704'
client = discord.Client()

# 起動時に表示
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# メッセージを受け取った時
@client.event
async def on_message(message):
    # botからのメッセージは無視
    if message.author.bot:
        return
    if message.content.startswith("!count"):
        #jsonファイルをロード
        download.download()
        json_open = open('COVID-19_data.json', 'r', encoding="utf-8_sig")
        json_load = json.load(json_open)
        jsn = json_load

        #居住都道府県名と数をdefaultdictで保持
        properties = defaultdict(int)
        for f in jsn['features']:
            property = f['properties']['居住都道府県']
            if property == '中華人民共和国' or property == '調査中' or property == '不明':
                continue
            if property not in properties:
                properties[property] = 0
            properties[property] += 1
        #一行ずつ出力すると時間がかかるので出力内容をあらかじめ保持
        say = ''
        for p in properties:
            say += p + ' ' + str(properties[p]) + '\n'
        await message.channel.send(say)

client.run(TOKEN)
