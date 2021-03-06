# -*- coding: utf-8 -*-
# Time    : 2020/8/5 19:06
# Author  : zlich
# Filename: JZ5-用两个栈实现队列.py
'''
用两个栈来实现一个队列，
完成队列的Push和Pop操作。
队列中的元素为int类型。
'''

'''
in 栈用来处理入栈（push）操作，out 栈用来处理出栈（pop）操作。
一个元素进入 in 栈之后，出栈的顺序被反转。
当元素要出栈时，需要先进入 out 栈，
此时元素出栈顺序再一次被反转，
因此出栈顺序就和最开始入栈顺序是相同的，
先进入的元素先退出，这就是队列的顺序。
'''


class Solution:
    def __init__(self):
        self.stackIn = []
        self.stackOut = []
    def push(self, node):
        self.stackIn.append(node)
    # write code here
    def pop(self):
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
        return self.stackOut.pop(0)
