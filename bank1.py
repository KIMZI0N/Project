#! /usr/bin/env python
#비밀번호 틀리면 출금, 송금 불가
#어떤 일을 얼마 했는지 프린트
class Account:
    def __init__(self,passwd,bal):
        self.__passwd = passwd
        self.__bal = bal
    def deposit(self, mon):
            self.__bal += mon
    def withdraw(self, mon, ipass):
        if ipass == self.__passwd:
            self.__bal -= mon
        else:
            print('password error!')
    def showBalance(self):
        return self.__bal
    def transfer(self, who, mon, ipass):
        if ipass == self.__passwd:
            self.__bal -= mon
            who.deposit(mon)
        else:
            print('password error!')

acc1 = Account('1234',1000)
acc1.deposit(1000)
acc1.withdraw(500, '1234')
print('account1\'s balance: ',acc1.showBalance())

acc2 = Account('0000',5000)
acc2.transfer(acc1, 1000, '0000')
print('account2\'s balance: ',acc2.showBalance())
print('account1\'s balance: ',acc1.showBalance())
