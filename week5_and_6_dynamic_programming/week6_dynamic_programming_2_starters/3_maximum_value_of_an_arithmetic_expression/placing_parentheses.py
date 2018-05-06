# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
def MinAndMax(oper, num, i, j, mini, maxi):
    min_, max_ = None, None
    for k in range(i, j):# 此处注意是不包括j，否则k+1会超出list的范围, oper[k]也会超出范围
        a = evalt(maxi[k][i], maxi[j][k+1], oper[k])# 此处意为，每个subsection被分成了i到k和k+1到j两部分
        b = evalt(mini[k][i], mini[j][k+1], oper[k])# 上限都是横轴上index，也就是第几个col。
        c = evalt(maxi[k][i], mini[j][k+1], oper[k])# 所以切记上限要写在前，也就是maxi[colNum][rowNum]
        d = evalt(mini[k][i], maxi[j][k+1], oper[k])# 这里是把这个subsection里面所有的运算符都试一次
        if min_ == None or max_ == None:# 每一次试都是把左最大VS右最大，左最大VS右最小，左最小VS右最大，左最小VS右最小都算出来
            min_ = min(a, b, c, d)# 然后找出他们最大值，最后从每个运算符中的最大值中找出究极最大值
            max_ = max(a, b, c, d)
        else:
            min_ = min(min_, a, b, c, d)
            max_ = max(max_, a, b, c, d)
    return min_, max_
def get_maximum_value(dataset):
    #write your code here
    num, oper = [], []
    for i in dataset:
        if i in ["+", "-", "*"]:
            oper.append(i)
        else:
            num.append(int(i))
    n = len(num)
    mini, maxi = [[0 for i in range(n)] for j in range(n)], [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        maxi[i][i], mini[i][i] = num[i], num[i]
    for s in range(1, n):# s必须从1开始，因为如果是0的话就会出现i=j的情况，这种情况在上一个loop都已经处理了
        for i in range(n-s):# j<=n-1，所以i+s在0到n-1之间0<=i<n-s
            j = i + s# 每轮i循环时候，j都是比i大一个固定的s值,所以是在一条斜线上增加
            mini[j][i], maxi[j][i] = MinAndMax(oper, num, i, j, mini, maxi)
    return maxi[n-1][0]


if __name__ == "__main__":
    print(get_maximum_value(input()))
# str = "0*8*3+3-7*2*1+6*3*8*0-8+1-2*7"
# print(get_maximum_value(str))

'''
/ test cases

0 --> 0

0+0 --> 0

9 --> 9

9*9 --> 81

1+5*6-3 --> 33

9*5*6-3 --> 267

1+1+1+1+1+1+1+1+1+1+1+1+1+1 --> 14

9*9*9*9*9*9*9*9*9*9*9*9*9*9 --> 22876792454961

9*9*9*9*9*9*9*9*9*9*9*9*9*9*9 --> 205891132094649

6*3-2-5+5+0+0+8-6*8+0-4-2+3+2 --> 1650

1+0+3*5+7-3*6*4-0-7+8-4*4*1*6 --> 149040

0*8*3+3-7*2*1+6*3*8*0-8+1-2*7 --> 181125
'''
