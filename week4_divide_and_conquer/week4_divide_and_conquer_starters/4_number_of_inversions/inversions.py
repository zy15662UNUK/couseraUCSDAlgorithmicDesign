# Uses python3

'''
When you merge two sorted part(I assume you have acknowledged the merge sort implementation),
you have sometimes need to use the right side part first, then that means a inversion is occurred,
but that's not simply occurred once,
it occurred (middle - i) times, middle is the middle index of current merge recursion, i is the index of left part.
'''
import sys
import random

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    nl, nr, ll, lr, n = ave - left, right - left, a[left: ave], a[ave: right], 0
    while len(ll) > 0 and len(lr) > 0:
        if ll[0] > lr[0]:
            number_of_inversions += len(ll)
            a[left + n] = lr[0]
            del(lr[0])
        else:
            a[left + n] = ll[0]
            del(ll[0])
        n += 1
    if len(ll) == 0:
        t = lr
    else:
        t = ll
    for i in range(len(t)):
        a[left + n + i] = t[i]
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
# def main():
#     n = random.randint(0, 10)
#     L = []
#     for i in range(n):
#         L.append(random.randint(0,100))
#     L = [9,8,7,3,2,1]
#     print("input: ",L)
#     print("results: ", get_number_of_inversions(L,len(L), 0, len(L)))
# main()
