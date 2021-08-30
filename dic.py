#! /usr/bin/env python

regNum0 ='951213-0000000'
regNum1 ='960125-0000000'
regNum2 ='970705-0000000'

d_year={}
d_day={}

d_year['Dec']=regNum0[2:4]
d_year['Jan']=regNum1[2:4]
d_year['Jul']=regNum2[2:4]
d_day['day1']=regNum0[4:6]
d_day['day2']=regNum1[4:6]
d_day['day3']=regNum2[4:6]

print('regNum0: ', list(d_year.keys())[0],'-',\
list(d_day.values())[0])
print('regNum1: ', list(d_year.keys())[1],'-',\
list(d_day.values())[1])
print('regNum2: ', list(d_year.keys())[2],'-',\
list(d_day.values())[2])
