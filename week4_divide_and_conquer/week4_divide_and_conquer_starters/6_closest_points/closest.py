#Uses python3
'''
delta indicates the smaller value of minDist_left and minDist_right. That means, in order to evaluate if there are two other points, one in the sub array Pl and the other in the sub array Pr whose distance is less than delta, we need to consider only those points in the array P that lie inside the region indicated with two vertical dashed lines, at the distance delta from the middle line.

So, what you need to do is go through the array P, and create a sub array containing only the points whose x coordinate lies inside the 2*delta region.

Now the cool part. Normally, if that region contains N points, you would have to perform N! calculations to check the distance of every point to all the other points, but, remember, we are only interested in those points whose distance is less than the already determined minimal distance delta.

That means, if this sub array is ordered by the y coordinates of the points, when you start looping through it in order to compare all the other distances, for every point you only need to check consecutive points whose vertical distance is less than the already determined minimal distance.
'''

import sys
import math

def cal_dis(m, n):
    return math.sqrt((m[0]-n[0])*(m[0]-n[0]) + (m[1]-n[1])*(m[1]-n[1]))

def findMinDis(points, l, r):
    if l + 2 == r:
        return min(cal_dis(points[l], points[r]), cal_dis(points[l+1], points[l]),cal_dis(points[l+1], points[r]))
    if l+ 1 == r:
        return cal_dis(points[l], points[r])
    mid = (l + r)// 2
    # print("mid: ", mid)
    l_min_dis = findMinDis(points, l, mid)
    r_min_dis = findMinDis(points, mid+ 1, r)
    # print("l_min_dis", l_min_dis)
    # print("r_min_dis", r_min_dis)
    # print("points[mid]", points[mid])
    min_of_two, newPoints = min(l_min_dis, r_min_dis), []
    for point in points[l: mid+1]:
        if point[0]> points[mid][0]- min_of_two:
            newPoints.append(point)
    for point in points[mid+ 1: r+ 1]:
        if point[0]< points[mid][0]+ min_of_two:
            newPoints.append(point)
    # print("min_of_two", min_of_two)
    # print("newPoints: ", newPoints)
    if(len(newPoints) <= 1):
        return min_of_two
    new_min_dis = cal_dis(newPoints[0], newPoints[1])
    newPoints.sort(key=lambda x: x[1])
    for i in range(len(newPoints)-1):
        if abs(newPoints[i][1]-newPoints[i+1][1])< min_of_two:
            dis = cal_dis(newPoints[i], newPoints[i+1])
            if dis< new_min_dis:
                new_min_dis = dis
    # print("new_min_dis", new_min_dis)
    return min(new_min_dis, min_of_two)

def minimum_distance(x, y):
    #write your code here
    points = []
    for i in range(len(x)):
        points.append((x[i], y[i]))
    points.sort(key=lambda x: x[0])
    res = findMinDis(points, 0, len(points) - 1)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
# x = [1,1]
# y = [2,2]
# print(minimum_distance(x, y))
