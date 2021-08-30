#! /usr/bin/env python

i=input('num op num = ')
l=i.split(' ')

num0=int(l[0])
op=l[1]
num1=int(l[2])

def clac(num0,num1,op):
    if op == '+':
        result = num0 + num1
        return result #함수의 진행이 끝남.
    elif op == '-':
        result = num0 - num1
        return result
    elif op == '*':
        result = num0 * num1
        return result
    elif op == '/':
        result = num0 / num1
        return result

print(f'{num0} {op} {num1} = {clac(num0,num1,op)}')
