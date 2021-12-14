## -*- coding: utf-8 -*-
from random import uniform

'''
В списке, состоящем из вещественных элементов, вычислить:
1. сумму элементов списка с нечетными номерами;
2. сумму элементов списка, расположенных между первым и последним отрицательными
элементами.
Сжать список, удалив из него все элементы, модуль которых не превышает 1.
Освободившиеся в конце списка элементы заполнить нулями.'
'''

arr = [round(uniform(-10, 10), 2) for _ in range(10)]
arr_2 = arr.copy()
summ = 0
check = 0
summ_1 = 0

for i in range(len(arr)):
    if i % 2 == 0:
        summ += arr[i]

for i in arr_2:
    if i > 0:
        arr_2.remove(i)
    else:
        break

arr_2 = arr_2[::-1]

for i in arr_2:
    if i > 0:
        arr_2.remove(i)
    else:
        break

for i in arr:
    if abs(i) < 1:
        arr.remove(i)
        arr.append(0)

print(*arr)
print(round(summ, 2))
print(round(sum(arr_2), 2))
