import json
import requests
from bs4 import BeautifulSoup
import datetime, time
from datetime import datetime

url= 'https://www.investing.com/equities/pre-market'
now = datetime.now()
timeCompare = now.replace(hour=5, minute=30)

# if now > timeCompare:
#     print("time is greater than 5:45")



r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')
mydivs = soup.find_all("div", {'class':'pt-2 font-normal PreMarketTopGainersLosersTable_cellSymbol__aSpNf'} )
print(mydivs)

class = 'datatable_cell__0y0eu datatable_cell--align-end__fwomz datatable_cell--up__Gt_ed datatable_cell--bold__UPfqK PreMarketTopGainersLosersTable_changePercent__By49D'
