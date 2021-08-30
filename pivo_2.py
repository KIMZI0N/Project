#! /usr/bin/env python

n_pivo = int(input('n_th pivo(n<3):'))
l_pivo = [0, 1]
print('len(l_pivo):', len(l_pivo))
#Use list and .append
def pivo(n):
    #for i in range(n - len(l_pivo)):
    while len(l_pivo) < n:
        l_pivo.append(l_pivo[-1] + l_pivo[-2])
    print(l_pivo[-1])
    print(l_pivo)
pivo(n_pivo)

#use function(재귀함수->오래걸림)
def pivo_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return pivo_r(n-1) + pivo_r(n-2)

print('pivo_r:', pivo_r(n_pivo -1))
