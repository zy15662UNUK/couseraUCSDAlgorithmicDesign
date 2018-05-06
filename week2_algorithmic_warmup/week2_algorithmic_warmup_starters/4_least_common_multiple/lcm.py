# Uses python3
import sys
# https://zh.wikihow.com/%E6%B1%82%E4%B8%A4%E4%B8%AA%E6%95%B0%E7%9A%84%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0
def gcd_naive(a, b):
    if min(a,b) == 0:
        return max(a,b)
    temp = max(a,b) % min(a,b)
    return gcd_naive(min(temp,min(a,b)),max(temp,min(a,b)))

def lcm_naive(a, b):
    return int((a*b)//gcd_naive(a,b))#use // for integer devision

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
# print(lcm_naive(226553150, 1023473145))
# python lcm.py
