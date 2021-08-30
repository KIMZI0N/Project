#! /usr/bin/env python

gugu = input('gugu?')

while not gugu.isdigit():
    gugu = input('gugu is not digit!:')

gugu = int(gugu)
#gugu is integer

while (2 <= gugu <= 19):
    gugu = input('[2,19]:')
gugu = int(guug)

for i in range(1, 10):
    dan = i * gugu
    print('{} * {} = {}'.format(gugu, i, dan))
