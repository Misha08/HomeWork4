## -*- coding: utf-8 -*-
from random import uniform

a, b = int(input()), int(input())
arr = [round(uniform(-10, 10), 2) for _ in range(10)]
arr_2 = arr[::-1]

for i in arr_2:
    if i < 0:
        arr_2.remove(i)
    else:
        break

print(max(arr))

for i in arr:
    if abs(i) > a and abs(i) < b:
        arr.remove(i)
        arr.append(0)

print(round(sum(arr_2), 2))
print(*arr)
