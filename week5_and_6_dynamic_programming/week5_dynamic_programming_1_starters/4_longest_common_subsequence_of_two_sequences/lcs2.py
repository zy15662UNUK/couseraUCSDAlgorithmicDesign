#Uses python3

import sys
def edit_distance(s, t):
    #write your code here
    len_i = len(s)
    len_j = len(t)
    col, D = [], []
    for i in range(len_j + 1):
        col.append(0)
    for i in range(len_i + 1):
        D.append(col[:])
    for j in range(1, len_j + 1):
        D[0][j] = j
    for i in range(1, len_i + 1):
        D[i][0] = i
    for j in range(1, len_j + 1):
        for i in range(1, len_i + 1):
            insert = D[i][j-1] + 1
            delete = D[i-1][j] + 1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1] + 1
            if s[i-1] == t[j-1]:
                D[i][j] = min(insert, delete, match)
            else:
                D[i][j] = min(insert, delete, mismatch)
        # print("i: ", i, "j: ", j, "D[i][j]: ",D[i][j])
    return D


# def lcs2(s, t):
#     #write your code here
#     D = edit_distance(s, t)
#     i, j, count = len(s), len(t), 0
#     while i > 0 or j > 0:
#         if i > 0 and D[i][j] == D[i-1][j] + 1:
#             i -= 1
#         elif j > 0 and D[i][j] == D[i][j-1] + 1:
#             j -= 1
#         else:
#             if s[i-1]==t[j-1] and i > 0 and j > 0:
#                count += 1
#             i -= 1
#             j -= 1
#     return count

def lcs2(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]# 创建(n+1)*(m+1)数组
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1): # loop every item in the matrix
        for j in range(n+1):
            if i == 0 or j == 0 : #因为相等只可能走对角线，所以第一排和第一列上都肯定是0
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:#如果原数组中两项相等，
                L[i][j] = L[i-1][j-1]+1#那么该处的相等点数目较左上角的加一
            else:#如果原数组中两项不等，那么它会是横向或者纵向移动
                L[i][j] = max(L[i-1][j] , L[i][j-1])#选取横向/纵向中相等点更多的方向
        print(L)

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#
#     n = data[0]
#     data = data[1:]
#     a = data[:n]
#
#     data = data[n:]
#     m = data[0]
#     data = data[1:]
#     b = data[:m]
#
#     print(lcs2(a, b))
a = [2,7,8,3]
b = [5,2,8,7]
print(lcs2(a, b))
