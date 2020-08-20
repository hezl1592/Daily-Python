# -*- coding: utf-8 -*-
# Time    : 2020/8/5 18:16
# Author  : zlich
# Filename: JZ1-二维数组中的查找.py
'''
题目描述
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

时间复杂度 O(M + N)，空间复杂度 O(1)。
其中 M 为行数，N 为 列数。 从二维数组右上角开始查找，
若target小于当前位置的值则应向左继续查找；
反之，若target大于当前位置的值则应向下查找
'''


def solve(array, num):
    if not array or not array[0] == 0:
        return False
    for row in array:
        if row[0] > num:
            continue
        else:
            if num in row:
                return True
    return False


if __name__ == '__main__':
    a = [[j for j in range(i * 10, i * 10 + 10)] for i in range(10)]
    print(a)
