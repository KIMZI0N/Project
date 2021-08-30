#! /usr/bin/env python

inStr = '10 USD, 5 EUR, 7 JPY, 9 CNY'
d_value = {
            'USD': 1203.82,
            'EUR': 1365.73,
            'JPY': 11.22,
            'CNY': 172.04
        }

inStr = inStr.replace(',','')
inStr = inStr.split(' ')
print(inStr)

