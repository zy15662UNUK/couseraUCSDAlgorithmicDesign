# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    n = len(w)
    result = [[0 for i in range(n+1)] for j in range(W+1)]
    for row in range(1, n+1):
        for col in range(1, W+1):
            result[col][row] = result[col][row-1]
            if w[row-1] <= col:
                res = result[col-w[row-1]][row-1] + w[row-1]
                result[col][row] = max(res, result[col][row-1])
    return result[W][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
# W = 10
# w = [3, 5, 3, 3, 5]
# print(optimal_weight(W, w))
