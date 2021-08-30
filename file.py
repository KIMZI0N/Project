#! /usr/bin/env python

FILE = open('./test_file.txt','w')

with open('./test_file.txt','r') as FI:
    for i in FI.readlines():
        print(i.strip())
    print('with out! Bye!')
print('hi')
