# Uses python3
import sys

def get_change(m):
    #write your code here
    n = 0
    while m > 0:
        if m >= 10:
            n += int((m - m%10)/10)
            m = m%10
        elif m >= 5:
            n += int((m - m%5)/5)
            m = m%5
        else:
            n += m
            m = 0

    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
# print(get_change(28))
# python change.py
