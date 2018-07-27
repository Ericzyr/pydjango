#!/usr/bin/env python3
# -*-coding:utf-8-*-
import os

t = os.listdir()
print(t)
t=os.getcwd()+'/v.sh'
print(t)
z=os.path.exists(t)
print(z)

if os.path.exists(t):
    os.remove(t)