#! /usr/bin/env python

class Cat:
    def snack(self):
        print('myeo~')

class KoShort(Cat):
    def setAge(self, Age):
        self.__age = Age
        print('set age to ', Age)
    
    def showAge(self):
        print(self.__age, 'years old.')

    def snack(self):
        print('야옹~')

minyong = KoShort()
minyong.setAge(7)
minyong.snack()
minyong.showAge()
print(minyong.__age)

