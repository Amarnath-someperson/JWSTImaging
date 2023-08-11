import json

jpgs = {}

f = open('raw/imagedetails.json')

json_ = json.load(f)
f.close()
jpgs['images'] = []
jpgs['descriptions'] = []
for i in json_['body']:
    if 'location' in i:
        # print(i['location'])
        if 'thumb' not in i['location']: # do not know if this is required, but thumbnails look rather small, so i have filtered them out
            jpgs['images'].append(i['location'])
            jpgs['descriptions'].append({'detail': i['details']['instruments'], 'description': i['details']['description']})

        # DOES NOT WORK THESE COMMENTED LINES DONT
        # for k in jpgs['images']:
        # jpgs['images'][k] = i['location']
        # jpgs['images'][v] = i['details']['description']
        # jpgs['images']['url'] = i['location']
        # jpgs['images']['description'] =i['details']['description']

# print(jpgs)
jsonout = json.dumps(jpgs, indent=4)

with open("raw/extest.json", "w") as outfile:
    outfile.write(jsonout)
