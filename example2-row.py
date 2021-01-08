import requests
from lxml import html
from string import Template
from pathlib import Path

ticker = 'TSLA'
link = 'https://www.marketwatch.com/investing/stock/tsla/financials'
locators_sales_revenue = Template('//div[normalize-space()="Sales/Revenue"]/../../td[${index}]//span')
locators_indexes = [2, 3, 4, 5, 6]
data_folder = "./data/example2"

Path(data_folder).mkdir(parents=True, exist_ok=True)

table = [['', '2015', '2016', '2017', '2018', '2019'],['Sales/Revenue']]

# load page
page = requests.get(link)
content = html.fromstring(page.content)

# gather data values to table
for i in locators_indexes:
    value = content.xpath(locators_sales_revenue.substitute(index=i))[0].text_content()
    table[1].append(value)

print(table)

# save data to csv file
with open(data_folder + '/' + ticker.upper() + '.csv', 'w') as f:
    for row in table:
        f.write(','.join(row))
        f.write("\n")

