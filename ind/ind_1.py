#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Ввести список А из 10 элементов, найти сумму элементов кратных 2, их количество и
#вывести результаты на экран.

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    sum = 0
    count = 0

    for id, val in enumerate(A):
        if val % 2 == 0:
            sum += val
            count += 1

    print("Сумма равна - ", sum, "\nКол-во равно - ", count)
