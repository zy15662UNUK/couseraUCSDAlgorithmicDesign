# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    a = 0
    b = 1
    count = 2
    while count <= n:
        temp = a + b
        a = b
        b = temp
        count += 1
    return b
n = int(input())
print(calc_fib(n))


# python fibonacci.py
