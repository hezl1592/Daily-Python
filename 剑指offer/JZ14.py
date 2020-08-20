# -*- coding: utf-8 -*-
# Time    : 2020/8/13 22:33
# Author  : zlich
# Filename: JZ14.py
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        first = head
        last = head
        while k > 1:
            if first.next:
                first = first.next
                k -= 1
            else:
                return None
        while first.next:
            last = last.next
            first = first.next
        return last


'''C++
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
        if (pListHead == nullptr || k ==0){
            return NULL;
        }
        ListNode* first = pListHead;
        ListNode* second = pListHead;
        for (int i=0; i<k-1;i++){
            if (first->next != NULL)
                first = first->next;
            else
                return NULL;
        }
        while (first->next!=NULL){
            first = first->next;
            second = second->next;
        }
        return second;
    }
};
'''
