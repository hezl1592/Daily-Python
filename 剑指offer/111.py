# -*- coding: utf-8 -*-
# Time    : 2020/8/16 19:49
# Author  : zlich
# Filename: 111.py

# data = list(map(int, '73 74 75 71 69 72 76 73'.split()))
#
# if max(data) == data[0]:
#
#
# for temp in enumerate:
data = [[10, 20], [30, 200], [400, 50], [30, 20]]
# while True:
#     in_ = input()
#     if len(in_)== 0:
#         break
#     indata = list(map(int, in_.split()))
#     data.append(indata)
    # if indata
# data = []
# while True:
#     in_ = input()
#     if len(in_)== 0:
#         break
#     indata = list(map(int, in_.split()))
#     data.append(indata)

disA, disB = 0,0
for i in range(len(data)//2):
    data.sort(key=lambda x:x[0])
    disA += data.pop(0)[0]
    data.sort(key=lambda x:x[1])
    disB += data.pop(0)[1]
print(str(disA + disB))