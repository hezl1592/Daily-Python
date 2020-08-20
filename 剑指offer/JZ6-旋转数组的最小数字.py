# -*- coding: utf-8 -*-
# Time    : 2020/8/9 16:41
# Author  : zlich
# Filename: JZ6-旋转数组的最小数字.py
'''
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

'''
解题思路
1.直接return min(array)....
2.二分法：
二分查找，如果中间元素位于递增元素，
那么中间元素>最右边元素，最小元素在后半部分。
否则，最小元素在前半部分。
'''


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        l, r = 0, len(rotateArray) - 1
        while l < r:
            mid = (r + l) // 2
            if rotateArray[mid] > rotateArray[r]:
                l = mid +1
            else:
                r = mid
        return rotateArray[l]