# -*- coding: utf-8 -*-
# Time    : 2020/8/15 8:38
# Author  : zlich
# Filename: JZ15-反转链表.py
'''
题目描述
输入一个链表，反转链表后，输出新链表的表头。
'''
'''
解题思路
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pre = None

        while pHead:
            next = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = next
        return pre


'''C++
class Solution {
public:
    ListNode* ReverseList(ListNode* pHead) {
        ListNode *pre = NULL;
        ListNode *next = NULL;
        while (pHead != NULL) {
            next = pHead->next;
            pHead->next = pre;
            pre = pHead;
            pHead = next;
        }
        return pre;
    }
};
'''
