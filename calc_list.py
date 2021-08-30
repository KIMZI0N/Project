#! /usr/bin/env python

i=input('num op num = ')
l=i.split(' ')
num0=int(l[0])
op=l[1]
num1=int(l[2])

list=['+','-','*','/']

def clac(num0,num1,op):
    if op == '+':
        result = eval(f'{num0} {list[0]} {num1}')
        return result
    elif op == '-':
        result = eval(f'{num0} {list[1]} {num1}')
        return result
    elif op == '*':
        result = eval(f'{num0} {list[2]} {num1}')
        return result
    elif op == '/':
        result = eval(f'{num0} {list[3]} {num1}')
        return result
print(i, '=', clac(num0,num1,op))
