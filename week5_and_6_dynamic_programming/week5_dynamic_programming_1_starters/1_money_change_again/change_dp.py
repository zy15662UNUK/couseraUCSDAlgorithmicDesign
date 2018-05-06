# Uses python3
import sys

def naive_get_change(m):
    #write your code here
    deno = [1, 3, 4]#list of coins
    if m == 0:      # amount = 0, change = 0
        return 0
    best = -1       # the min num to be compared
    for i in deno:
        if i <= m:
            newBest = get_change(m - i) + 1 # recursion back to the previous min num of change, 1 here repre i
        if best <= 0:
            best = newBest
        else:
            best = min(best, newBest)
    return best

def get_change(m):
    #write your code here
    deno, minCoin = [1, 3, 4], {0: 0}
    for t in range(1, m+1): # starts from amount 1, increase to desire value in steps. cal min for each step by
        best = -1           # refer to the previous cases(min(t-1), min(t-3), min(t-4))
        for i in deno:
            if i <= t:
                newBest = minCoin[t - i] + 1
            if best < 0:
                best = newBest
            else:
                best = min(best, newBest)
        minCoin[t] = best
    return minCoin[m]
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
# print(get_change(34))
