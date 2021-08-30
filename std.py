#! /usr/bin/env python

kor = input('input korean score: ')
eng = input('input english score: ')
mat = input('input math score: ')

class Student:
    def __init__(self,K,E,M):
        self.__korean = K
        self.__english = E
        self.__math = M
        self.__avg = round((int(K)+int(E)+int(M))/3, 2)
    def showKorean(self):
        return self.__korean
    def showEnglish(self):
        return self.__english
    def showMath(self):
        return self.__math
    def showAverage(self):
        return self.__avg

std = Student(kor,eng, mat)

print('korean score: ',std.showKorean())
print('english score: ', std.showEnglish())
print('math score: ', std.showMath())
print('average: ', std.showAverage())
