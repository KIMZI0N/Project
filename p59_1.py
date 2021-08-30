#! /usr/bin/env python

toCount = 'We tried list and we tried dicts also we tried Zen'
d_Count = dict()

l_toCount = toCount.split()

for key in l_toCount: #단어리스트
    if key not in d_Count: #딕셔너리 키 유무
        d_Count[key] = 1 #없으면 1
    else:
        d_Count[key] += 1 #있으면 +1

for i in d_Count: #딕셔너리 for문에 넣으면 키가 i로 들어감.
    print(i, d_Count[i])
'''
for k, v in d_Count.items():
    print(k,v)
'''
