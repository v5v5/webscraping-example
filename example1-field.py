import requests
from lxml import html
from pathlib import Path

ticker = 'TSLA'
link = 'https://www.marketwatch.com/investing/stock/tsla/financials'
locator_sales_revenue2019 = '/html/body/div[3]/div[5]/div/div[2]/div/div/table/tbody/tr[1]/td[6]/div/span'
data_folder = "./data/example1"

Path(data_folder).mkdir(parents=True, exist_ok=True)

page = requests.get(link)
content = html.fromstring(page.content)
value = content.xpath(locator_sales_revenue2019)[0].text_content()

print(value)

# create table with data
table = [['', '2019'],['Sales/Revenue', value]]
print(table)

# save data to csv file
with open(data_folder + '/' + ticker.upper() + '.csv', 'w') as f:
    for row in table:
        f.write(','.join(row))
        f.write("\n")


