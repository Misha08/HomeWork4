## -*- coding: utf-8 -*-
from random import randint

'''
Ввести список А из 10 элементов, найти наименьший элемент и переставить его с
последним элементом. Преобразованный список вывести.
'''

arr = [randint(1, 10) for _ in range(10)]
last = arr[0]
arr[0], arr[-1] = min(arr), last
print(arr)