# -*- coding: utf-8 -*-
# Time    : 2020/8/9 17:34
# Author  : zlich
# Filename: JZ8-跳台阶.py
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''

'''
对于第n阶台阶来说，有两种办法，一种是爬一个台阶，到第n-1阶；
第二种是爬两个台阶，到第n-2阶。

f(n) = f(n-1) + f(n-2)
'''


class solution:
    def jumpFloor(self, number):
        if number <= 0:
            return 0
        result = [1, 2]
        if number <= 2:
            return result[number - 1]
        for i in range(2, number):
            result.append(result[i - 1] + result[i - 2])
        return result[-1]


'''C++
class Solution {
public:
    int jumpFloor(int number) {
        if (number <= 0)
            return 0;
        if (number <= 2)
            return number;
        int first = 1, second=2;
        int result = 0;
        for (int i =3; i<=number; i++){
            result = first+second;
            first = second;
            second = result;
        }
        return result;
    }
};
'''
