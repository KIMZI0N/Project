#! /usr/bin/env python

fp = open('./fileIO.txt','r')
fp_list = fp.readlines()
for i in range(0,len(fp_list),2):
    print(fp_list[i+1],end='')

