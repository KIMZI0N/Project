#! /usr/bin/env python

inStr = '10 USD, 5 EUR, 7 JPY, 9 CNY'

d_value = {
            'USD': 1203.82,
            'EUR': 1365.73,
            'JPY': 11.22,
            'CNY': 172.04
        }

usd = (d_value['USD'])*int(inStr[0:2])
eur = int(inStr[0:2])
usd = int(inStr[0:2])
usd = int(inStr[0:2])

#outStr = str(usd) + 'KRW'

print(type(d_value['USD']))


