#! /usr/bin/env python

score =int(input('score= '))

if (90 <= score) and (score <= 100):
    grade = 'A'
elif (80 <= score) and (score <= 89):
    grade = 'B'
elif (70 <= score) and (score <= 79):
    grade = 'C'
elif (60 <= score) and (score <= 69):
    grade = 'D'
elif score <= 59:
    grade = 'F'
else:
    grade = 'incorrent score'

print(grade)
