# Uses python3
import sys
# Only store the last digit save a lot of time
# https://stackoverflow.com/questions/40094796/python-calculate-the-last-digit-of-a-large-fibonacci-number-with-less-time
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    count = 2
    while count <= n:
        temp = (a+b)%10
        a = b
        b = temp
        count += 1
    return b


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
# print(get_fibonacci_last_digit_naive(999999))
# python fibonacci_last_digit.py
