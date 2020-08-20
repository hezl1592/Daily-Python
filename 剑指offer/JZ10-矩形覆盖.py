# -*- coding: utf-8 -*-
# Time    : 2020/8/12 8:54
# Author  : zlich
# Filename: JZ10-矩形覆盖.py
'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
比如n=3时，2*3的矩形块有3种覆盖方法：
'''

'''
解题思路f(n) = f(n-1) + f(n-2)
'''


class solution:
    def rectCover(self, number):
        if number <= 0:
            return 0
        if number <= 2:
            return number
        a, b = 1, 2
        for i in range(3, number):
            a, b = b, a + b
        return b


'''C++
class Solution {
public:
    int rectCover(int number) {
        if(number <=0)
            return 0;
        if(number<=2)
            return number;
        int a=1, b=2;
        for (int i =3; i<=number; i++){
            int temp = b;
            b = a+b;
            a = temp;
        }
        return b;
    }
};
'''
