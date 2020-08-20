# -*- coding: utf-8 -*-
# Time    : 2020/8/12 9:19
# Author  : zlich
# Filename: JZ11-二进制中1的个数.py

class solution:
    def NumberOf1(self, n):
        state = n & 0xFFFFFFFF
        return bin(state).count('1')