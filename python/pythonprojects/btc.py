import os, json
from requests import request, Session
import requests
api = 'acf07e01-8a46-452f-8f89-6bf4016c873a'
api_url = "http://pro-api.coinmarketcap.com/v1/tools/price-conversion"

parameters = {
'amount':'1',
'symbol':'BTC',
'convert':'USD'
}

headers = {
'Accepts': 'application/json',
'X-CMC_PRO_API_KEY': api,
}

session = Session()
session.headers.update(headers)

resp = session.get(api_url, params=parameters)
price = "{}".format(json.loads(resp.text)['data']['quote']['USD']['price'])
print(price)
# data = {'Value1':price}
# ifttt = 'https://maker.ifttt.com/trigger/btc_price/json/with/key/dXDn1zXUmTXFYoz0cmfv0r'
# requests.post(ifttt, json=data)

