# Uses python3
import sys
import math
def binary_search(a, x):
    left, right = 0, len(a)-1
    # write your code here
    while left <= right:
        mid = math.ceil((left+right)/2)
        if a[mid] > x:
            right = mid -1
        elif a[mid] < x:
            left = mid + 1
        elif a[mid] == x:
            return mid
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')

# import random
# n = random.randint(0,30)
# a = []
# for i in range(n):
#     a.append(random.randint(0,100))
# for i in range(10):
#     x = random.randint(0,100)
#     print("x = ", x)
#     print("result: ", binary_search([1, 5, 8, 10, 12, 13], 1))
