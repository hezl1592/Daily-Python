# -*- coding: utf-8 -*-
# Time    : 2020/8/9 16:17
# Author  : zlich
# Filename: JZ4-.py

'''
题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和
中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

'''
前序遍历第一个值为根节点的值，
这个值将中序遍历序列中的值分为左右两部分，
其中左边为左子树中序遍历结果，右边为右子树中序遍历结果。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution:
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre.pop(0))
        n = tin.index(root.val)  # 找到根节点在中序遍历中的位置
        root.left = self.reConstructBinaryTree(pre, tin[:n])
        root.right = self.reConstructBinaryTree(pre, tin[n + 1:])
        return root
