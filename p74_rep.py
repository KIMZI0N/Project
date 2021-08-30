#! /usr/bin/env python

inSeq = input('Give Me Sequence!: ')
cSeq = inSeq.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
CSeq = cSeq.upper()

if (CSeq == inSeq[::-1]):
    print('{} is palindromic'.format(inSeq))
else:
    print('{} is not palindromic'.format(inSeq))
