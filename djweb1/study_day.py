#!/usr/bin/env python3
# -*-coding:utf-8-*-


dic ={'k1': 'java', 'k2': 'python', 'k3': 'shell'}


user_list = [
    {'user': "jack","pwd":"adc"},
    {'user': "tom","pwd":"Adc"},
]

for i, v in dic.items():
    print(i, v)





for li in user_list:
    print(li['user'], li['pwd'])