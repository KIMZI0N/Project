#! /usr/bin/env python

inStr = '10 USD, 5 EUR, 7 JPY, 9 CNY'

d_value = {
            'USD': 1203.82,
            'EUR': 1365.73,
            'JPY': 11.22,
            'CNY': 172.04
        }

inStr = inStr.split(',')
VALUE0 = inStr[0].strip().split()[0]
TYPE0 = inStr[0].strip().split()[1]
VALUE1 = inStr[1].strip().split()[0]
TYPE1 = inStr[1].strip().split()[1]
VALUE2 = inStr[2].strip().split()[0]
TYPE2 = inStr[2].strip().split()[1]
VALUE3 = inStr[3].strip().split()[0]
TYPE3 = inStr[3].strip().split()[1]

RESULT0 = int(VALUE0) * d_value[TYPE0]
RESULT1 = int(VALUE1) * d_value[TYPE1]
RESULT2 = int(VALUE2) * d_value[TYPE2]
RESULT3 = int(VALUE3) * d_value[TYPE3]

outStr = ' KRW, '.join([str(RESULT0), str(RESULT1), str(RESULT2), str(RESULT3)]) + ' KRW'
print(outStr)
