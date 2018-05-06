# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)
b=0
b_index=0
c=0
for i in range(0, n):
    if (a[i]>b):
        b=a[i]
        b_index=i
for i in range(0, n):
    if (a[i]<=b) & (a[i]>c) & (i != b_index):
   		c=a[i]

result = c*b
print(result)
