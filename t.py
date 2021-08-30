#! /usr/bin/env python

dol = input('입력:')
s = dol.split()

if s[1]=='달러':
    print(int(s[0])*1167)
elif s[1]=='엔':
    print(int(s[0])*1.096)
elif s[1]=='유로':
    print(int(s[0])*1268)
elif s[1]=='위안':
    print(int(s[0])*171)
