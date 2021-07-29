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

    time_now = time.strftime('%Y-%m-%d %H:%M:%S')  # gets system time

    bpi = data_json['bpi']  
    bpi_eur = bpi['EUR']  # gets eur price from coindesk json response
    price_eur = bpi_eur['rate']
    
    bpi_usd = bpi['USD']  # gets usd price from api
    price_usd = bpi_usd['rate']
    
    bpi_gbp = bpi['GBP']  # gets gbp price from api
    price_gbp = bpi_gbp['rate']
    
    price_eur = price_eur.replace(',', '')  # removes comma and converts to float
    price_eur = float(price_eur)
    price_usd = price_usd.replace(',', '')
    price_usd = float(price_usd)
    price_gbp = price_gbp.replace(',', '')
    price_gbp = float(price_gbp)

    data = [time_now, price_eur]  # select currency to be added to csv
    writer.writerow(data)

    f.close()

    print('OK', time_now)  # Prints a message every loop for debugging

    time.sleep(600)
