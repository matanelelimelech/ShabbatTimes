#get specipic info from url

import json
import requests

cities = [294801, 281184, 293397, 295530]
result = requests.get('https://www.hebcal.com/shabbat?cfg=json&amp;lg=h&;M=on;&b=on&geonameid=294801')
data = json.loads(result.text)

print(data['date'])
print(data['items'][1]['title'])
print(data['location']['city'])
print(data['items'][0]['title'])
print(data['items'][2]['title'])

result = requests.get('https://www.hebcal.com/shabbat?cfg=json&amp;lg=h&;M=on;&b=on&geonameid=281184')
data = json.loads(result.text)

print(data['location']['city'])
print(data['items'][0]['title'])
print(data['items'][2]['title'])

result = requests.get('https://www.hebcal.com/shabbat?cfg=json&amp;lg=h&;M=on;&b=on&geonameid=293397')
data = json.loads(result.text)
print(data['location']['city'])
print(data['items'][0]['title'])
print(data['items'][2]['title'])

result = requests.get('https://www.hebcal.com/shabbat?cfg=json&amp;lg=h&;M=on;&b=on&geonameid=295530')
data = json.loads(result.text)
print(data['location']['city'])
print(data['items'][0]['title'])
print(data['items'][2]['title'])

# print(data['items'][]['title'])

# for item in data['items']:
 # print(item['title'])


