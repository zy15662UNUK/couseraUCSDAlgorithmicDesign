'''
partition()
x ← A[ℓ] {pivot}
j ← ℓ
for i from ℓ + 1 to r:
if A[i ] ≤ x:
j ← j + 1
swap A[j ] and A[i ]
{A[ℓ + 1 . . . j ] ≤ x, A[j + 1 . . . i ] > x}
swap A[ℓ] and A[j ]
return j
'''

def partition(A, l, r):
    # partition is to find the index to "break" the array into two
    pivot = A[l]
    j = l
    for i in range(l+1, r+1):
        if A[i] <= pivot:
            j += 1
            A[i], A[j] = A[j], A[i]
    A[j], A[l] = A[l], A[j]
    return j

def quickSort(A, l, r):
    while l < r:
        m = partition(A, l, r)
        # do partition first
        # then recursion starts at the short side
        if (m-l) < (m-r):
            quickSort(A, l, m-1)
            l = m+1
        else:
            quickSort(A, m+1, r)
            r = m - 1
    return A

import random
def main():
    n = random.randint(0, 50)
    L = []
    for i in range(n):
        L.append(random.randint(0,1000))
    print(quickSort(L,0,n-1))
main()
# python quick_sort.py
