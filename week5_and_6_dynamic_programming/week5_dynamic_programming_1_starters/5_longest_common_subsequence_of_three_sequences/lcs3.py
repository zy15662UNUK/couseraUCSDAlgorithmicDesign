#Uses python3

import sys
def lcs3(X, Y, Z):
    m = len(X)
    n = len(Y)
    o = len(Z)
    L = [[[0 for i in range(o+1)] for j in range(n+1)]
         for k in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if (i == 0 or j == 0 or k == 0):
                    L[i][j][k] = 0

                elif (X[i-1] == Y[j-1] and
                      X[i-1] == Z[k-1]):
                    L[i][j][k] = L[i-1][j-1][k-1] + 1

                else:
                    L[i][j][k] = max(max(L[i-1][j][k],
                    L[i][j-1][k]),
                                    L[i][j][k-1])

    # L[m][n][o] contains length of LCS for
    # X[0..n-1] and Y[0..m-1] and Z[0..o-1]
    return L[m][n][o]
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
# a = [3, 5, 4, 34, 2, 56, 4, 7, 32, 5, 6, 3]
# b = [2, 3, 2, 4, 7, 32, 4, 5, 6, 4]
# c = [2, 4, 7, 32, 5, 3]
# print(lcs3(a, b, c))
