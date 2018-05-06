#Uses python3

import sys

def sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j]<list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list
def max_dot_product(a, b):
    #write your code here
    a = sort(a)
    b = sort(b)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
# print(max_dot_product([23], [39]))
# python dot_product.py
