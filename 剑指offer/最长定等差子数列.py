# -*- coding: utf-8 -*-
# Time    : 2020/8/19 14:40
# Author  : zlich
# Filename: 最长定等差子数列.py
def printarray(arr):
    print('--' * 10)
    for ar in arr:
        print(ar)


def solve(arr, diff):
    dp = [[1 for j in range(len(arr) + 1)] for i in range(len(arr) + 1)]
    for i in range(1, len(arr) + 1):
        dp[i] = dp[i - 1][:]
        for j in range(i, 0, -1):
            if arr[i - 1] - arr[j - 1] == diff:
                print(i - 1, '-', j - 1, ":", arr[i - 1], arr[j - 1])
                dp[i][i] = max(dp[i][i], dp[i][j] + 1)
            printarray(dp)
    a = set()
    for dp1 in dp:
        dp1 = dp1[::-1]
        print(dp1)
        a.add(dp1[:-1].index(max(dp1[:-1])))
    print(a)
    print()
    max_x = [d[1:].index(max(d[1:])) for d in dp[1:]]
    print(max_x)
    print(set([d[1:].index(max(d[1:][::-1])) for d in dp[1:]]))
    print([arr[i] for i in set([d[1:].index(max(d[1:])) for d in dp[1:]])])


if __name__ == '__main__':
    arr = [2, 3, 5, 5, 6, 7, 8, 9]
    solve(arr, 1)
