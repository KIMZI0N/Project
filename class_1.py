#! /usr/bin/env python

class Person:
    nation = 'A nation'
    def greeting(self, a):
        a.hi2()
        print('(method)greeting:', 'Hi')

    def hi1(self):
        self.greeting()

    def hi2(self):
        greeting()

def greeting():
    print('(function)greeting:', 'Hello!')

yune = Person()
yune1 = Person()
yune.greeting(yune1) # == yune.greeting(yune,yune1)
print()

