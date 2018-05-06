# Uses python3
import sys

def fibonacci(n):#get nth fibonacci number
    if n <= 1:
        return n
    previous = 0
    current  = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
 # find Pisano period first
    t = 1
    previous = 0
    current  = 1
    while True:
        if (current%m == 0) and ((current+previous)%m == 1):#period starts with 01
            break
        previous, current = current, previous + current
        t += 1
    return fibonacci(n%(t))%m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
# print(get_fibonacci_huge_naive(239,1000))
# python fibonacci_huge.py
