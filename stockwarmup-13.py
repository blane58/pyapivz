#!/usr/bin/python3

import requests
import pprint

def main():
    with open("/home/student/apikeys/alphavantage.apikey") as apikey:
        myapikey = apikey.read()

    mylookup = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&nterval=5min&apikey=" + myapikey
    stockdata = requests.get(mylookup)
    decodedstockdata = stockdata.json()
    lastrefreshed = stockdata.json()["Meta Data"]["3. Last Refreshed"]
    ##pprint(decodedstockdata["Time Series (5min)"]["2019-08-20 10:35:00"])
    ##pprint.pprint(lastrefreshed)
    ##pprint.pprint(stockdata.json())

    cryptolookup = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=" + myapikey

    crypto = requests.get(cryptolookup)
    cryptojson = crypto.json()
    pprint.pprint(cryptojson['Realtime Currency Exchange Rate']['2. From_Currency Name'])
    pprint.pprint(cryptojson['Realtime Currency Exchange Rate']['4. To_Currency Name'])
    pprint.pprint(cryptojson['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    

main()

