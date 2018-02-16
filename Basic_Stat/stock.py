# coding: utf-8
import csv

with open('tab_delimited_stock_prices.txt', 'r') as f:
   reader = csv.reader(f, delimiter = '\t')
   for row in reader:
       date = row[0]
       symbol = row[1]
       closing_price = float(row[2])
       # process(date, symbol, closing_price)


with open('colon_delimited_stock_prices.txt', 'r') as f:
    reader = csv.DictReader(f, delimiter = ':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        # process(date, symbol, closing_price)

today_prices = {'AAPL':90.91, 'MSFT':41.68, 'FB':64.5}       
with open('comma_delimited_stock_prices.txt', 'w') as f:
    writer = csv.writer(f, delimiter = ',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])

        
    
