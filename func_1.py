#! /usr/bin/env python

def book_0(name, age, book1, book2):
    print('name: {0} age: {1}'.format(name, age), end = ' ')
    print('book:', book1, book2)

def book_1(name, age, *books):
    print('name: {0} age: {1}'.format(name, age), end = ' ')
    print('book:', end = ' ')
    for book in books:
        print(book, end = ' ')
    print()

book_0('zion', 5, 'python', 'basic')
book_1('zion', 5, 'python', 'basic')
book_1('zion', 5, 'python', 'basic', 'photo')

#book_0('zion', 5, 'python', 'basic', 'photo')
