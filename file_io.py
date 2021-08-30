#! /usr/bin/env python

fp = open('./dataFile.txt','r')
fp_read = fp.read()
print(fp_read)
fp.close()

fp = open('./dataFile.txt','r')
fp_readline1 = fp.readline()
print(fp_readline1)
fp_readline2 = fp.readline()
print(fp_readline2)
fp.close()

fp=open('./dataFile.txt','r')
while True:
    fp_line = fp.readline()
    if not fp_line:
        break
    print(fp_line, end='')
