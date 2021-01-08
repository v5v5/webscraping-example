# Цель: хотим найти компьютер с оптимальным (лучшим) процессором и оптимальной (лучшей) ценой

# - перейдем на сайт /www.ozon.ru > Электроника > Компьютеры > Системные блоки
# - отфильруем по размеру скидку
# - получим такой url https://www.ozon.ru/category/sistemnye-bloki-15704/?sorting=discount
# - скопируем данные в файл

from pathlib import Path
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

link = 'https://www.ozon.ru/category/sistemnye-bloki-15704/?sorting=discount'

xpath_card = "//*[@class='a0c4']"
# xpath_name = "//*[@class='a0c4']//*[contains(@class,'a2g0')]"
xpath_name = ".//*[contains(@class,'a2g0')]"
# xpath_processor = "//*[@class='a0c4']//*[contains(text(),'Процессор')]//font[1]"
xpath_processor = ".//*[contains(text(),'Процессор')]//font[1]"
xpath_discount = ".//*[contains(@class,'a0x0')]"
xpath_price = ".//*[contains(@class,'b5v6')]"
xpath_oldprice = ".//*[contains(@class,'b5v9')]"
table = []

data_folder = "./data/example7"
Path(data_folder).mkdir(parents=True, exist_ok=True)

options = Options()
options.headless = True
driver = webdriver.Chrome("c:/chromedriver.exe", options=options)
driver.implicitly_wait(1000)
driver.get(link)
cards = driver.find_elements_by_xpath(xpath_card)

for c in cards:
    computer_name = c.find_elements_by_xpath(xpath_name)[0].text
    print(computer_name)
    computer_processor = c.find_elements_by_xpath(xpath_processor)[0].text
    hz = re.search(r'\((.*?) ГГц', computer_processor).group(1)

    discounts = c.find_elements_by_xpath(xpath_discount)
    discount = discounts[0].text if len(discounts) > 0  else ''
    computer_price = c.find_elements_by_xpath(xpath_price)[0].text

    computer_oldprices = c.find_elements_by_xpath(xpath_oldprice)
    computer_oldprice = computer_oldprices[0].text if len(computer_oldprices) > 0  else ''

    if (computer_name in [item[0] for item in table]):
        continue

    table.append([])
    table[len(table) - 1].append(computer_name)
    table[len(table) - 1].append(computer_processor)
    table[len(table) - 1].append(hz)
    table[len(table) - 1].append(discount)
    table[len(table) - 1].append(computer_price)
    table[len(table) - 1].append(computer_oldprice)

    # print(computer_name)
    # print(computer_processor)
    # print(hz)

# save data to csv file
with open(data_folder + '/' + 'computers.csv', 'w', encoding="utf-8") as f:
    for row in table:
        f.write(';'.join(row))
        f.write("\n")

driver.quit()



