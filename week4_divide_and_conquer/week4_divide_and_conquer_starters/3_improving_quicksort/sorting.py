# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x, j, k = a[l], l, l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
            if a[j] == x:
                k += 1
                a[k], a[j] = a[j], a[k]
    # swap the "pivots" to the "break point"
    count = 0
    for i in range(k - l + 1):
        a[l + i], a[j - count] = a[j - count], a[l + i]
        count += 1
    return (j - count+1, j)

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, n + 1, r)
    return a

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
# import random
# def main():
#     n = random.randint(0, 10)
#     L = []
#     for i in range(n):
#         L.append(random.randint(0,15))
#     L = [10,9,8,7,6,5]
#     print("res: ", randomized_quick_sort(L, 0, len(L) - 1))
# main()
