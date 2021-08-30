#! /usr/bin/env python

class Animal:
    def __init__(self,M,H,S):
        self.master = M
        self.home = H
        self.sex = S
    def feed(self,a):
        if a == 1:
            #print('Thank you')
            return('Thank you')
        elif a == 0:
            #print('Im hungry')
            return('Im hungry')
Que = Animal('ks','sev','male')
print(Que.master)
print(Que.home)
print(Que.sex)
print(Que.feed(1))

Que = Animal('ks','sev','female')
print(Que.sex)
