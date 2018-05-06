# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    string = "011235831459437077415617853819099875279651673033695493257291"#Pisano period. for mod 10
    result=int(string[(n+2)%60])-1
    if result >= 0:
        return result
    else:
        return 9

def fibonacci_partial_sum_naive(from_, to):
    lowerSum = fibonacci_sum_naive(from_-1)
    upperSum = fibonacci_sum_naive(to)
    if from_ == 0:
            return upperSum
    if upperSum >= lowerSum:
        return upperSum-lowerSum
    else:
        return upperSum-lowerSum+10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
# print(fibonacci_partial_sum_naive(0,0))
# python fibonacci_partial_sum.py
