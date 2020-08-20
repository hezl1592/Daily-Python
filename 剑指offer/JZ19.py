# -*- coding: utf-8 -*-
# Time    : 2020/8/15 12:29
# Author  : zlich
# Filename: JZ19.py

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        out = []
        if not matrix:
            return out
        visited = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
        directs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        start = [0, 0]
        out.append(matrix[0][0])
        visited[0][0] = True
        for i, d_temp in enumerate(directs):
            if i % 2 == 0:
                ro = len(matrix[0])
            else:
                ro = len(matrix)
            for i in range(ro-1):
                start[0] += d_temp[0]
                start[1] += d_temp[1]
                print("...", start)
                if start[0] >= 0 and start[0] <= len(matrix) - 1 and start[1] >= 0 and start[1] <= len(matrix[0]) - 1:
                    if visited[start[0]][start[1]] == False:
                        out.append(matrix[start[0]][start[1]])
                        visited[start[0]][start[1]] = True
            print(visited)
        return out

if __name__ == '__main__':
    a = Solution()
    x = a.printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    print(x)