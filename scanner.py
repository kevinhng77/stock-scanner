import json
import os
from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import datetime, time
from datetime import datetime

url= 'https://www.investing.com/equities/pre-market'
now = datetime.now()
timeCompare = now.replace(hour=5, minute=30)

def callNow():
    if now > timeCompare:
        account_sid = "AC0dcd3d24de7ea7b04a8174dc18e22179"
        auth_token = "31ada64acedb8e0211fd9f9e2c5ffed6"
        client = Client(account_sid, auth_token)

        call = client.calls.create(
        url="http://demo.twilio.com/docs/voice.xml",
        to="+14152603133",
        from_="+18449292123"
        )

        print(call.sid)

# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'html5lib')
# mydivs = soup.find_all("div", {'class': 'PreMarketTopGainersLosersTable_wrapper__NWnQ0'} )
# print(mydivs)


callNow()