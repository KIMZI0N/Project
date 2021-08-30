#! /usr/bin/env python

string = 'We tried list and we tried dicts also we tried Zen'

list=string.split()
s=set(list)
dic = {}
for i in s:
    dic[i]=list.count(i)
for k, v in dic.items():
    print(k, v)
