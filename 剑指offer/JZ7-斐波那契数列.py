# -*- coding: utf-8 -*-
# Time    : 2020/8/9 17:17
# Author  : zlich
# Filename: JZ7-斐波那契数列.py
class solution:
    def Fibonacci(self, n):
        if n <= 0:
            return 0
        a = b = 1
        for i in range(2, n):
            a, b = b, a + b
        return b


'''C++
class Solution {
public:
    int Fibonacci(int n) {
        if (n < 2)
            return n;
        int a=0;
        int b = 1;
        for (int i=2; i<=n; i++){
            int temp = a;
            a = b;
            b = temp + b;
        }
        return b;
    }
};
'''
