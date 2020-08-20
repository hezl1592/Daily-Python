# -*- coding: utf-8 -*-
# Time    : 2020/8/9 17:44
# Author  : zlich
# Filename: JZ9-变态跳台阶.py
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……
它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

'''
解题思路：f(n) = f(n-1) + f(n-2) + f(n-3) ... +f(1) + 1
'''


class Solution:
    def jumpFloorII(self, number):
        if number <= 0:
            return 0
        result = [1, 2]
        if number <= 2:
            return number
        for i in range(3, number + 1):
            result.append(sum(result) + 1)
        return result[-1]
