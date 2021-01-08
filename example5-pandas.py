import pandas as pd
from string import Template
from pathlib import Path

# tickers = ['tsla']
tickers = ['tsla', 'msft', 'ntla', 'edit', 'crsp']
link = Template('https://www.marketwatch.com/investing/stock/${ticker}/financials')
data_folder = "./data/example5"

Path(data_folder).mkdir(parents=True, exist_ok=True)

for ticker in tickers:
    print(f'Ticker: {ticker.upper()}')

    # read table with data from webpage
    df = pd.read_html(link.substitute(ticker=ticker), displayed_only = False)[4]

    # delete duplicated values in columns and cells
    df.rename(lambda x : x.split('  ')[0] , axis='columns', inplace = True)
    df['Item'] = df['Item'].apply(lambda x : x.split('  ')[0])

    # save to csv file
    df.to_csv(data_folder + '/' + ticker.upper() + '.csv', index = False)
    # df.to_html(data_folder + '/' + ticker.upper() + '.html', index = False)
    # df.to_excel(data_folder + '/' + ticker.upper() + '.xlsx', index = False)
