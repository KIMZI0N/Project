#! /usr/bin/env python

regNum0 = '951213-0000000'
regNum1 = '960125-0000000'
regNum2 = '970705-0000000'

d_mon = {
        '01':'Jan',
        '07':'Jul',
        '12':'Dec'
         }

prt0 = d_mon[regNum0[2:4]] + '-' + regNum0[4:6]
prt1 = d_mon[regNum1[2:4]] + '-' + regNum1[4:6]
prt2 = d_mon[regNum2[2:4]] + '-' + regNum2[4:6]

print('regNum0:',prt0)
print('regNum1:',prt1)
print('regNum2:',prt2)

