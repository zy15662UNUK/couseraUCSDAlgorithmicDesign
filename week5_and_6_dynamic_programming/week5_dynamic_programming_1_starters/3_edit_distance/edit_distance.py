# Uses python3
def edit_distance(s, t):
    #write your code here
    len_i = len(s)
    len_j = len(t)
    col, D = [], []
    for i in range(len_j + 1):
        col.append(0)
    for i in range(len_i + 1): #构建一个二维数组，len(j)*len(s)的矩阵
        D.append(col[:])
    for j in range(1, len_j + 1):
        D[0][j] = j
    for i in range(1, len_i + 1):
        D[i][0] = i
    for j in range(1, len_j + 1): #循环矩阵中每一项
        for i in range(1, len_i + 1):
            insert = D[i][j-1] + 1#分别考察四种可能的操作情况
            delete = D[i-1][j] + 1
            match = D[i-1][j-1] #match和mismatch的特征一样，都是指向左上角
            mismatch = D[i-1][j-1] + 1
            if s[i-1] == t[j-1]: #如果是match
                D[i][j] = min(insert, delete, match)#三种操作中操作数最少的
            else:#如果是mismatch
                D[i][j] = min(insert, delete, mismatch)
        # print("i: ", i, "j: ", j, "D[i][j]: ",D[i][j])
    return D[len_i][len_j]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
# print(edit_distance("short", "ports"))
