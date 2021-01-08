import requests
from lxml import html
from string import Template
from pathlib import Path

# ticker = 'TSLA'
ticker = 'msft'
link = Template('https://www.marketwatch.com/investing/stock/${ticker}/financials')
locators_financials = "//div[@class='financials']//table//tr/td[1]/div[2]"
locators_value = Template('./../../td[${index}]//span')
locators_indexes = [2, 3, 4, 5, 6]
data_folder = "./data/example3"

Path(data_folder).mkdir(parents=True, exist_ok=True)
table = [['Item', '2016', '2017', '2018', '2019', '2020']]

# load page
page = requests.get(link.substitute(ticker=ticker))
content = html.fromstring(page.content)

# gather data values to table
for locator_financial in content.xpath(locators_financials):
    financial_name = locator_financial.text_content()
    print(financial_name)
    table.append([])
    table[len(table) - 1].append(financial_name)
    for i in locators_indexes:
        value = locator_financial.xpath(locators_value.substitute(index=i))[0].text_content()
        print(value)
        table[len(table) - 1].append(value)

print(table)

# save data to csv file
with open(data_folder + '/' + ticker.upper() + '.csv', 'w') as f:
    for row in table:
        f.write(','.join(row))
        f.write("\n")

