from twilio.rest import Client
account_sid = 'AC9e4120ed8c67d56694404691d647aa9e'
auth_token = '0fee436091a1e789c9318a7709f98780'
phone_numbers = (['+972524560626'], ['+972526506946'])
Client = Client(account_sid, auth_token)


import json
import requests


def send_sms(x):
    print(x)

    Client.messages.create(
        to='+972526506946',
        from_="+15087097328",
        body=(x)
    )

cities = ['294801', '281184', '293397', '295530']
for id in cities:
    result = requests.get("https://www.hebcal.com/shabbat?cfg=json&amp;lg=h&;M=on;&b=on&geonameid="+id)
    data = json.loads(result.text)

    text = data['items'][1]['title'] + "\n" + data['location']['city'] + "\n" +data['items'][0]['title'] + "\n" + data['items'][2]['title']
    send_sms(text)