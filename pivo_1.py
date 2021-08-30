#! /usr/bin/env python

n=int(input('n_th pivo: '))
list=[0,1]
sum=1

def pivo(n):
    

for i in range(2,n+1,1):
    sum = list[i-1] + list[i-2]
    list.append(sum)

print(list[n-1])
print(list)
n=int(input('n_th pivo: '))

