# Uses python3
import sys

def optimal_sequence(n):
    if n == 1:
        return [1]
    dic = {1: {"val": 0, "prev": None}}#初始化中间值存储，val是最小中间操作步骤数，prev指向上一个中间值
    for i in range(2, n+1): #从2开始直到n，计算每一个数的最小中间操作数
        min_ = [] #用来存储*3，*2，+1三种情况的中间操作数，每个的操作数的值等于之前中间值的操作数+1
        if i% 3 == 0:
            min_.append({"val": dic[int(i/ 3)]["val"]+ 1, "key": int(i/ 3)})#存储中间操作数和上一个中间值
        if i% 2 == 0:
            min_.append({"val": dic[int(i/ 2)]["val"]+ 1, "key": int(i/ 2)})
        min_.append({"val": dic[i- 1]["val"]+ 1, "key": i- 1})
        min_.sort(key=lambda x: x["val"])#按照中间操作值从小到大排列
        prev = min_[0]["key"]#设置指向上一个中间值的指针
        dic[i] = {"val": min_[0]["val"], "prev": prev}#放入中间值存储
    res = [n]
    pointer = dic[n]["prev"]
    while pointer != None:#按照指针从后往前查找中间值，直到遇到第一项1为止
        res.append(pointer)
        last = dic[pointer]
        pointer = last["prev"]
    res.reverse()
    return res

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

# n = 96234
# print(optimal_sequence(n))
# 1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
