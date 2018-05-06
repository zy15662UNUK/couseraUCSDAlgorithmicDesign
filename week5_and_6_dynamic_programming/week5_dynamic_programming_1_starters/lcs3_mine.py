#Uses python3
'''
这题本质上和上一题相同，只不过将数组换成三维的，思路和上题同
注意此处for循环构建三维数组的简写方式
'''
import sys
def lcs3(a, b, c):
    #write your code here
    m = len(a)
    n = len(b)
    p = len(c)
    '''
    此处注意：构建数组必须是：最内层长度: len(c)+1, 次内层长度: len(b)+1, 最外层长度len(a)+1
    这个顺序不可改变， 否则会通不过最后一个测试题
    '''
    l = [[[None for j in range(p+1)] for i in range(n+1)] for k in range(m+1)]
    for i in range(m+1): # loop every item in the matrix
        for j in range(n+1):
            for k in range(p+1):
                if i == 0 or j == 0 or k == 0: #因为相等只可能走对角线，所以第一排和第一列上都肯定是0
                    l[i][j][k] = 0
                elif a[i-1] == b[j-1] and b[j-1]== c[k-1]:#如果原数组中两项相等，
                    l[i][j][k] = l[i-1][j-1][k-1]+1#那么该处的相等点数目较左上角的加一
                else:#如果原数组中两项不等，那么它会是横向或者纵向移动
                    l[i][j][k] = max(l[i-1][j][k] , l[i][j-1][k], l[i][j][k-1],l[i-1][j-1][k], l[i-1][j][k-1], l[i][j-1][k-1])
                    #选取横向/纵向中相等点更多的方向
            # print(L)
    return l[m][n][p]
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
