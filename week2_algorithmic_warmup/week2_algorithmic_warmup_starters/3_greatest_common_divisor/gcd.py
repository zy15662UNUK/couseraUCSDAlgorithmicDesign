# Uses python3
import sys

def gcd_naive(a, b):
    if min(a,b) == 0:
        return max(a,b)
    temp = max(a,b) % min(a,b)
    return gcd_naive(min(temp,min(a,b)),max(temp,min(a,b)))


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
# print(gcd_naive(28851538, 1183019))
# python gcd.py
