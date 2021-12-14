## -*- coding: utf-8 -*-
from random import randint

'''
Ввести список А из 10 элементов, найти наибольший элемент и переставить его с первым
элементом. Преобразованный список вывести.
'''

arr = [randint(1, 10) for _ in range(10)]
last = arr[0]
arr[0], arr[-1] = max(arr), last
print(arr)