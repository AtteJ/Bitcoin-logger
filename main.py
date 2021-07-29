import csv
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

    time_now = time.strftime('%Y-%m-%d %H:%M:%S')

    bpi = data_json['bpi']
    bpi_eur = bpi['EUR']
    price_eur = bpi_eur['rate']
    
    price_eur = price_eur.replace(',', '')  # removes comma and converts to float
    price_eur = float(price_eur)

    data = [time_now, price_eur]
    writer.writerow(data)

    f.close()

    print('OK', time_now)  # Prints a message every loop for debugging

    time.sleep(600)
