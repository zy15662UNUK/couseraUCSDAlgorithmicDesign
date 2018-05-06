# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')
def sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if (list[j].start)>(list[j+1].start):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list
def optimal_points(segments):
    points = []
    segments = sort(segments)
    #write your code here
    i = 0
    while True:
        if i >= len(segments):
            break
        t = 0
        print(i)
        while segments[i].end >= segments[i+t].start:
            if t > len(segments)-i-1:
                break
            else:
                t += 1
        points.append(segments[i].end)
        print(points)
        i += t

    return points

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *data = map(int, input.split())
#     segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
#     points = optimal_points(segments)
#     print(len(points))
#     for p in points:
#         print(p, end=' ')
points = optimal_points([Segment(4, 7),Segment(1, 3),Segment(2, 5),Segment(5, 6)])
print(len(points))
for p in points:
    print(p, end=' ')
# python covering_segments.py
