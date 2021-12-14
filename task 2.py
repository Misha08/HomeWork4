## -*- coding: utf-8 -*-
from random import randint

'''
# Ввести список А из 10 элементов, найти произведение положительных элементов и вывести
# его на экран.
'''

arr = [randint(-10, 10) for _ in range(10)]
multip = 1

for i in arr:
    if i > 0:
        multip *= i
        
print(multip)