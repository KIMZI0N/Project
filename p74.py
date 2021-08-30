#! /usr/bin/env python

inSeq = input('Give Me Sequence!: ')
d_nuc1 = { 'A':'T', 'T':'A', 'C':'G', 'G':'C'}
outSeq=''

for i in inSeq[::-1]:
    outSeq += d_nuc1[i]

if (outSeq == inSeq):
    print('{} is palindromic'.format(inSeq))
else:
    print('{} is not palindromic'.format(inSeq))
