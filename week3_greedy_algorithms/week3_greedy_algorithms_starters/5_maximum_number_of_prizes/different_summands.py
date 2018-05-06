# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    a = 1
    while n > 0:
        if n-a > a:
            summands.append(a)
            n -= a
            a += 1
        else:
            summands.append(n)
            n = 0
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
# summands = optimal_summands(2)
# print(len(summands))
# for x in summands:
#     print(x, end=' ')
# python different_summands.py
