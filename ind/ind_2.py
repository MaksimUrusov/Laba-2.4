#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#16. В списке, состоящем из вещественных элементов, вычислить:
#1. количество положительных элементов списка;
#2. сумму элементов списка, расположенных после последнего элемента, равного нулю.

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    pol = 0

    for id, val in enumerate(A):
        if val > 0:
            pol += val

    sum = 0

    for i in range(len(A) - 1, 0, -1):
        if A[i] != 0:
            sum += A[i]
        else:
            break
    print(pol, sum)