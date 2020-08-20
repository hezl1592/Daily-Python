# -*- coding: utf-8 -*-
# Time    : 2020/8/5 18:31
# Author  : zlich
# Filename: JZ3-从尾到头打印链表.py
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        out = []
        if listNode is None:
            return out
        while listNode.next is not None:
            out.append(listNode.val)
            listNode = listNode.next

        out.append(listNode.val)
        return out[::-1]
        # write code here


if __name__ == '__main__':
    head = ListNode(0)
    temp = head
    for i in range(1,9):
        new = ListNode(i)
        temp.next = new
        temp = temp.next
    print(head.val, head.next.val, head.next.next.val)