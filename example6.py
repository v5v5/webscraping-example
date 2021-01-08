import pandas as pd
from string import Template
from pathlib import Path
import requests

# tickers = ['tsla']
tickers = ['boss']
# tickers = ['tsla', 'msft', 'ntla', 'edit', 'crsp']
with open('tickers-1.csv') as f:
    tickers = f.read().splitlines()

print(tickers)

link = Template('https://www.marketwatch.com/investing/stock/${ticker}/financials')
data_folder = "./data/example6"

Path(data_folder).mkdir(parents=True, exist_ok=True)

for ticker in tickers:
    print(f'Ticker: {ticker.upper()}')

    # read table with data from webpage
    try:
        page = requests.get(link.substitute(ticker=ticker))
        if page.history:
            print(f'Data is not available for ticker {ticker.upper()}')
            continue
        content = pd.read_html(link.substitute(ticker=ticker), displayed_only = False)
        df = content[4]
    except:
        print(f'Data is not available for ticker {ticker.upper()}')
        continue

    # delete duplicated values in columns and cells
    df.rename(lambda x : x.split('  ')[0] , axis='columns', inplace = True)
    df['Item'] = df['Item'].apply(lambda x : x.split('  ')[0])

    # save to csv file
    df.to_csv(data_folder + '/' + ticker.upper() + '.csv', index = False)