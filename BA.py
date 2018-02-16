#!/bin/python3

import sys


def buyMaximumProducts(n, k, a):
    # Complete this function
    x = []
    i = 0
    res = 0
    while (len(x) != len(a) and k > 0):
        mini = a[i]
        minInd = i
        for j in range(i, n):
            if a[j] < mini:
                mini = a[j]
                minInd = j

        a[minInd] = 101
        i = 0
        x.append([mini, minInd + 1])
        if k >= x[-1][0] * x[-1][1]:
            res += x[-1][1]
            k -= (x[-1][0] * x[-1][1])
        else:
            res += int(k / x[-1][0])
            k -= int(k / x[-1][0]) * x[-1][0]
    return res


if __name__ == "__main__":
    f=open("input.txt","r")
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split(' ')))
    k = int(f.readline().strip())
    result = buyMaximumProducts(n, k, arr)
    print(result)
