#! /usr/bin/env python

chicken = 10

def countChicken(people):
    chicken =20
    chicken -= people
    print(chicken, 'chicken remained')

def countChicken_global(people):
    global chicken
    chicken -= people
    print(chicken, 'chicken remained')

print('chicken:', chicken)
countChicken(5)
print('chicken:', chicken)
print()
print('chicken:',chicken)
countChicken_global(5)
print('chicken',chicken)
