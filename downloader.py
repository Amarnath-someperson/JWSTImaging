import requests
import json

f = open('raw/extest.json')
images = json.load(f)
f.close()
index = images['images'][0].index('.com/') +5
x=0
for url in images['images']:
    r = requests.get(url, allow_redirects=True)
    name = images['images'][x][index:]
    open('raw_images/'+name, 'wb').write(r.content)
    x+=1