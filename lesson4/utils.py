
from decimal import *
from datetime import datetime
from requests import get


def currency_rates(money):
    address = get('http://www.cbr.ru/scripts/XML_daily.asp').text.split("</Valute>")
    money = money.upper()
    for i in address:
        if i.count(money):
            nominal = (int(i[i.find('<Nominal>') + len('<Nominal>'):i.find('</Nominal>')]))
            value = (float(i[i.find('<Value>') + len('<Value>'):i.find('</Value>')].replace(',', '.')))
            value = Decimal(str(value))
            return f"{nominal} {money} = {value} рублей"