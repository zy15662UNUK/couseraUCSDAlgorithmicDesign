# Uses python3
import sys
import itertools

def optimal_weight(W, w):# DP方法找出能不能从数组A中找出数使他们和为给定的和
# 和上一题原理一样
    # write your code here
    n = len(w)
    result = [[0 for i in range(n+1)] for j in range(W+1)]
    for row in range(1, n+1):
        for col in range(1, W+1):
            result[col][row] = result[col][row-1]
            if w[row-1] <= col:
                res = result[col-w[row-1]][row-1] + w[row-1]
                result[col][row] = max(res, result[col][row-1])
    col, row, res = W, n, []
    while col > 0 and row > 0:# 从最后一项开始回溯,分最后一项被用上和最后一项没被用上两种情况讨论
        if result[col-w[row-1]][row-1] + w[row-1] > result[col][row-1]:
            res.append(w[row-1])
            col, row = col-w[row-1], row-1
        else:
            row -= 1

    return result[W][n], res# 返回最终得出的和,以及用上的数

def partition3(A):
    A.sort(reverse=True)#将A先从小到大排好,确保在DP中有多个解时优先返回含有较大数的那个解.
    # 例如A = [ 1, 1, 1, 2, 2, 2 ],理应返回1([1,2][1,2][1,2]),
    # 如果不排序会在第一个返回[1,1,1]导致最终返回0
    if sum(A) % 3 != 0: # 如果list不能被3整除,那他必然不能被分为和相等三份
        return 0
    W = sum(A) // 3# 每份和的值
    res1, list1 = optimal_weight(W, A)
    if res1 != W:# 如果从这些数中凑不出和为W,那么直接返回0
        return 0
    for i in list1:# 如果从这些数中凑出和为W,那么去掉用过的数再看能不能从剩下的里面凑出来
        A.remove(i)
    res2, list2 = optimal_weight(W, A)
    if res2 != W:# 如果从这些数中凑不出和为W,那么直接返回0
        return 0
    return 1# 如果从这些数中凑出和为W,那么不用检查第三组,必然是可以的,直接返回1
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
# A = [ 1, 1, 1, 2, 2, 2 ]
# print(partition3(A))
