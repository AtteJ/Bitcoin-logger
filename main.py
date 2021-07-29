import csv
import requests
import json
import dateutil.parser
import time
from urllib.request import urlopen

url = "https://api.coindesk.com/v1/bpi/currentprice/EUR.json"  # Coindesk api url

while True:
    f = open('bitcoin.csv', 'a')  # Opens a precreated csv file, add header manually
    writer = csv.writer(f)

    r = urlopen(url)
    data_json = json.loads(r.read())

    time_data = data_json['time']
    time_iso = time_data['updatedISO']
    time_parsed = dateutil.parser.isoparse(time_iso)

    bpi = data_json['bpi']
    bpi_eur = bpi['EUR']
    price_eur = bpi_eur['rate']
    
    price_eur = price_eur.replace(',', '')  # removes comma and converts to float
    price_eur = float(price_eur)

    data = [time_parsed, price_eur]
    writer.writerow(data)

    f.close

    print('OK')  # Prints a message every time loop runs for debugging

    time.sleep(600)
