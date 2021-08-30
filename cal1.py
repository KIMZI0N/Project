#! /usr/bin/env python

inStr = '10 USD, 5 EUR, 7 JPY, 9 CNY'

d_value = {
            'USD': 1203.82,
            'EUR': 1365.73,
            'JPY': 11.22,
            'CNY': 172.04
        }
inStr = inStr.split(',')

usd = round(int(inStr[0][:2])*d_value['USD'],2)
eur = int(inStr[1][:2])*d_value['EUR']
jpy = int(inStr[2][:2])*d_value['JPY']
cny = int(inStr[3][:2])*d_value['CNY']

outStr = str(usd) + ' KRW,' + str(eur) + ' KRW,' + str(jpy) + ' KRW,' + str(cny) + ' KRW'

print(outStr)
