'''
merge(B, C)
D ← empty array of size p + q
while B and C are both non-empty:
b ← the first element of B
c ← the first element of C
if b ≤ c:
move b from B to the end of D
else:
move c from C to the end of D
move the rest of B and C to the end of D
return D
'''
'''
mergeSort(A)
if n = 1:
return A
m ← ⌊n/2⌋
B ← MergeSort(A[1 . . .m])
C ← MergeSort(A[m + 1 . . . n])
A′ ← Merge(B, C)
return A′
'''
import math
import random
def merge(B, C):
    res = []
    while (len(B) != 0) and (len(C) != 0):
        if B[0] > C[0]:
            res.append(C[0])
            del(C[0])
        else:
            res.append(B[0])
            del(B[0])
    if len(B) == 0:
        res += C
    else:
        res += B
    return res
def mergeSort(A):
    n = len(A)
    if n == 1:
        return A
    mid = math.floor(n/2)
    B = mergeSort(A[0:mid])
    C = mergeSort(A[mid:n])
    res = merge(B, C)
    return res
def main():
    n = random.randint(0, 1000)
    L = []
    for i in range(n):
        L.append(random.randint(0,1000))
    print("input: ",L)
    print("results: ", mergeSort(L))
main()
# python merge_sort.py
