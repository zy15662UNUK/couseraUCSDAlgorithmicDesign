#Uses python3
# for all the case if x>y, number xy > yx

import sys

# pick the "greatest" number
def func(x):
    temp = x[0]
    for i in range(1,len(x)):
        a = str(x[i])
        b = str(temp)
        if int(a+b)>= int(b+a):
            temp = x[i]
    return temp
def largest_number(a):
    #write your code here
    res = ""
    b = a[:]
    for x in a:
        add = func(b)
        res += str(add)
        b.remove(add)
    return res
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

# print(largest_number([9,4,6,1,9]))
# python largest_number.py
