name = input('what is your name: ')

class Person:   
    nation = ''

    def showNation(self):
        print('your nation is ',self.nation,'!')

    def setNation(self,n):
        self.nation=d_persons[n]

d_persons = {'name0':'nation0','name1':'nation1','name2':'nation2','name3':'nation3'}  

inst = Person()
inst.setNation(name)
inst.showNation()
print(name)
