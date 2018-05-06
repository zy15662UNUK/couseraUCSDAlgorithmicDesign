# Uses python3
'''
"a hint. For each point xi consider a pair (xi, 'p').
Fore each segment [ai,bi] consider two pairs: (ai, 'l') and (bi, 'r') (p, l, r stand for point, left, and right, respectively).
This gives you p+2s pairs. Define an order on such pairs and sort the pairs with respect to this order."

upd: Finally understand:)
The trick is to sort lefts of segments and find not greater than point and rights and find not less than point.
And then think how this correlate with the answer
'''
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    all, count = [], {"l": 0, "r": 0}
    for i in range(len(starts)):
        all.append({"val": starts[i], "type": "l"})
        all.append({"val": ends[i], "type": "r"})
    for i in range(len(points)):
        all.append({"val": points[i], "type": "p", "index": i})
    def func(el):
        if el["type"] == "l":
            return el["val"]
        elif el["type"] == "p":
            return el["val"] + 0.1
        else:
            return el["val"] + 0.2
    all.sort(key=func)
    # print("all2: ",all)
    for i in range(len(all)):
        if all[i]["type"] == "l":
            count["l"] += 1
        elif all[i]["type"] == "r":
            count["r"] += 1
        else:
            cnt[all[i]["index"]] = count["l"] - count["r"]
        # print("count: ", count,"all[i]: ", all[i])
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
