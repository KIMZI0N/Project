#! /usr/bin/env python

dic = {
        'a_str' : 'Apple!',
        'b_list' : [1,2,3,4],
        'c_tuple' : ('a','b','c'),
        'd_dict' : {1:'one', 2:'two'}
      }
print('dic:',dic)
print('dic_a:',dic['a_str'])
print('dic_b:',dic['b_list'])
print('dic_b0:',dic['b_list'][0])
print('dic_b1:',dic['b_list'][1])
print('dic_b2:',dic['b_list'][2])
print('dic_b3:',dic['b_list'][3])
print('dic_c:',dic['c_tuple'])
print('dic_d:',dic['d_dict'])
print('dic_d1:',dic['d_dict'][2])
