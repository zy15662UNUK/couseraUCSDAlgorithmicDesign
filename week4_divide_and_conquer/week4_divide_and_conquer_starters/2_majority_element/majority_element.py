# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    a = sorted(a)
    count, max_, check = 1, 1, len(a)/2
    while left < right - 1:
        left += 1
        if a[left] == a[left - 1]:
            count += 1
            max_ = max(count, max_)
        else:
            max_ = max(count, max_)
            count = 1
    if max_ > check:
        return max_
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
# a = [1,2,2,1,2,1]
# print(get_majority_element(a, 0, len(a)))
