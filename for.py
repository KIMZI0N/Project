#! /usr/bin/env python

while(True):
    j = input('input your number(2~19):')
    while not j.isdigit():
        j = input("is not number!:")

    j = int(j)
    if 1 < j < 20:
        for i in range(1,10,1):
            print("%d * %d = %d"%(j,i,j * i))
        break
    else:
        print('is not in range!')
        continue    
