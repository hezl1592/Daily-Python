# -*- coding: utf-8 -*-
# Time    : 2020/8/15 9:44
# Author  : zlich
# Filename: JZ17-树的子结构.py
'''
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot2:
            return False


        while