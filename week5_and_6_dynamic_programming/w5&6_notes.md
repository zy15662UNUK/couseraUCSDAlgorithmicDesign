- Making change visualization by David Galles: https://www.cs.usfca.edu/~galles/visualization/DPChange.html

1. How many insertions are needed to make axybc from abc?
  2: Insert x between a and b, then y between x and b.

2. What is the edit distance between words bread and really?
  4: Delete b, then change d to l, then insert l and y in the end.

3. What is the edit distance between bread and really if it is allowed to insert and delete symbols, but forbidden to replace symbols?
  5: Remove b, remove d, insert l, l and y.

4. We want to compute not only the edit distance d between two words, but also the number of ways to edit the first word to get the second word using the minimum number d of edits. Two ways are considered different if there is such i,1≤i≤d that on the i-th step the edits in these ways are different.

To solve this problem, in addition to computing array T with edit distances between prefixes of the first and second word, we compute array ways, such that ways[i,j] = the number of ways to edit the prefix of length i of the first word to get the prefix of length j of the second word using the minimum possible number of edits.

Which is the correct way to compute ways[i,j] based on the previously computed values?

```
ways[i, j] = 0
if T[i, j] == T[i - 1, j] + 1:
  ways[i, j] += ways[i - 1, j]
if T[i, j] == T[i, j - 1] + 1:
  ways[i, j] += ways[i, j - 1]
if word1[i] == word2[j] and T[i, j] == T[i - 1, j - 1]:
  ways[i, j] += ways[i - 1, j - 1]
if T[i, j] == T[i - 1, j - 1] + 1:
  ways[i, j] += ways[i - 1, j - 1]

  T[i,j] is computed based on T[i−1,j], T[i,j−1] and T[i−1,j−1]: we decide what will be the last edit and then try to use the minimum number of edits needed before that, which is already stored in the table T for all the variants of the last editing action. If the minimum number of edits T[i,j] can be obtained via different last editing actions, we should sum all the ways that exactly T[i,j] edits can be made to change the i-th prefix of the first word into the j-th prefix of the second word.

  First if checks all the ways when the last action is to delete the last symbol. Second if checks all the ways when the last action is to insert the necessary symbol. Third if checks all the ways to match last symbols of the prefixes. Last if checks all the ways to replace the last symbol of the i-th prefix of the first word by the last symbol of the j-th prefix of the second word.


```

- D(i, j)=
  insertions: D(i , j − 1) + 1
  Delete: D(i − 1, j ) + 1
  match: D(i − 1, j − 1) + 1
  mismatch/replace: D(i − 1, j − 1)


- Q1: changes problem, naive recursion VS. dynamic programming(store each steps):
 dynamic programming one:

 loop from 1 to input m
    loop coin in coins:
      if coin <= money
       changes value of current money = changes value of (current money - coin) + 1
    store the min changes value of current money
  return min changes value of m money


- Q2: How to avoid exceed maximum memory

don't store list of lists, it will consume lots of memory. Store pointer to previous one for each

So the idea is to build an array of best previous pointers for all numbers from 1 to n. Let's say now n is 10. The best previous pointers will look like:

Num:        1   2   3   4   5   6   7   8   9

pointer:  None  1   1   3   4   3   1   4   3

- Q3:
EditDistance(A[1 . . . n], B[1 . . .m]):
    D(i , 0) ← i and D(0, j) ← j for all i , j # 第一横排和第一竖列分别是单纯的insert和delete，所以操作数等于序号数
    for j from 1 to m: # 外层必须是第二个字符串
      for i from 1 to n:
        insertion ← D(i , j − 1) + 1# 分别考察移动到点i，j的四种可能情况对应的操作数大小
        deletion ← D(i − 1, j) + 1
        match ← D(i − 1, j − 1)
        mismatch ← D(i − 1, j − 1) + 1
        if A[i ] = B[j ]:# 选出四种操作中最小的
          D(i , j) ← min(insertion, deletion, match)
        else:
          D(i , j) ← min(insertion, deletion, mismatch)
    return D(n,m)
``

- Q4:  find longest common subsequence: 相当于统计两串字符中matches的数量

```
def lcs2(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]# 创建(n+1)*(m+1)数组
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1): # loop every item in the matrix
        for j in range(n+1):
            if i == 0 or j == 0 : #因为相等只可能走对角线，所以第一排和第一列上都肯定是0
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:#如果原数组中两项相等，
                L[i][j] = L[i-1][j-1]+1#那么该处的相等点数目较左上角的加一
            else:#如果原数组中两项不等，那么它会是横向或者纵向移动
                L[i][j] = max(L[i-1][j] , L[i][j-1])#选取横向/纵向中相等点数目更多的方向
        print(L)

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
```

- Q5:

```
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
                else:#如果原数组中两项不等，那么它会是x向或者y向移动或者z向移动
                    l[i][j][k] = max(l[i-1][j][k] , l[i][j-1][k], l[i][j][k-1],l[i-1][j-1][k], l[i-1][j][k-1], l[i][j-1][k-1])
                    #选取x向/y向/z向中相等点更多的方向
    return l[m][n][p]
```


- Greedy仅适用于continuous的knapsack problem, 也就是每个物体可以只拿一部分而不是全部。
  但是对于discrete的knapsack，也就是每个物体不可分割，不适用

- knapsack with repetition:当总质量为W的时候，其value可以是val(W-wi)+vi,其中wi, vi为质量不大于W的物体质量，value。所以对于每个W，仅需要loop出比W小的wi，找出拿走wi后的最大价值，然后加上vi得出value，在这些value中找出最大值即是该W下的最大value。这个value会在求以后更大的W时被引用到

```
value(0) ← 0<!-- 初始化，质量为0时value也是0.这种仅需要1*(W+1)的矩阵就好 -->
for w from 1 to W:<!-- 对于每一个最大质量w -->
  value(w) ← 0<!-- 先默认当前质量下的value是0 -->
  for i from 1 to n:<!-- 对于每一个可能的最后一个物体的-->
    if wi ≤ w:<!-- 只有当wi比总质量w小时，才存在wi是最后一个放进包里物品可能性 -->
      val ← value(w − wi ) + vi<!-- 假设wi是包里最后放进来物品，看这种情况下质量为w，数量为i的value是多少 -->
      if val > value(w):<!-- 如果这种情况的value更大 -->
        value(w) ← val<!-- 那么就令“wi是包里最后放进来物品”这个情况是“包质量为w，数量为i”的价值 -->
return value(W)
```
- knapsack without repetition:比上面的要复杂一些，因为有两种情况：1. 包里已有物品wi，这时候和上面一样只需要看value(W-wi)+vi 2. 包里并没有物品wi, 那么value(w, i) ← value(w, i − 1)
- value(w, i )is the maximum value achievable using a knapsack of weight w and items 1, . . . , i

 ```
 Knapsack(W)
  initialize all value(0, j) ← 0 <!-- 初始为一个(n+1)*(W+1)的矩阵 -->
  initialize all value(w, 0) ← 0  <!-- n是背包里item数目，W是背包能装质量上限 -->
  <!-- 一排排的填写矩阵 -->
  for i from 1 to n:<!-- 对于每一种item数量i -->
    for w from 1 to W:<!-- 对于每一个最大质量w -->
      value(w, i) ← value(w, i − 1)<!-- 先假设ith item不在包中，也就value等效于包质量为w，但是包里物品只有i-1个的情况 -->
      if wi ≤ w:<!-- 只有当wi比总质量w小时，才存在wi是最后一个放进包里物品可能性 -->
        val ← value(w − wi , i − 1) + vi<!-- 假设wi是包里最后放进来物品，看这种情况下质量为w，数量为i的value是多少 -->
        if value(w, i ) < val<!-- 如果wi是包里最后放进来物品的value大于不是最后放进来物品的value -->
          value(w, i ) ← val<!-- 那么就令“wi是包里最后放进来物品”这个情况是“包质量为w，数量为i”的价值 -->
  return value(W, n)
 ```

- parentheses() algorithm:

```
MinAndMax(i , j)<!-- 用于计算从数i到数j能产出的最大最小值 -->
  min ← +∞
  max ← −∞
  for k from i to j − 1: <!-- 从i到j-1,按照每个运算符把算式分成两份,计算大大,大小,小大,小小四种组合的结果 -->
    a ← M(i , k) opk M(k + 1, j )
    b ← M(i , k) opk m(k + 1, j )
    c ← m(i , k) opk M(k + 1, j )
    d ← m(i , k) opk m(k + 1, j )
    min ← min(min, a, b, c, d)
    max ← max(max, a, b, c, d)<!-- 更新最大值最小值 -->
  return (min, max)
```

```
Parentheses(d1 op1 d2 op2 . . . dn)
<!-- 初始化两个n*n矩阵,一个存放最大值,一个存放最小值,纵轴为i,横轴为j -->
  for i from 1 to n:
    m(i , i ) ← di, M(i , i ) ← di<!-- i=j时,也就是对角线上值,由于只有一个数,所以最大最小值都是本身 -->
  for s from 1 to n − 1:
    for i from 1 to n − s:
      j ← i + s<!-- 对于每一个j>i的点,计算从数i到数j能产出的最大最小值 -->
      m(i , j ),M(i , j ) ← MinAndMax(i , j )
  return M(1, n)<!-- 最终结果是数i到数n最大值/ -->
```
- Q1:

```
def optimal_weight(W, w):
    # write your code here
    n = len(w)
    result = [[0 for i in range(n+1)] for j in range(W+1)]
    for row in range(1, n+1):
        for col in range(1, W+1):
            result[col][row] = result[col][row-1]
            if w[row-1] <= col:
                res = result[col-w[row-1]][row-1] + w[row-1]
                result[col][row] = max(res, result[col][row-1])
    return result[W][n]

```
- Q2:

```
def optimal_weight(W, w):# DP方法找出能不能从数组A中找出数使他们和为给定的和
# 和上一题原理一样
    # write your code here
    n = len(w)
    result = [[0 for i in range(n+1)] for j in range(W+1)]
    for row in range(1, n+1):
        for col in range(1, W+1):
            result[col][row] = result[col][row-1]
            if w[row-1] <= col:
                res = result[col-w[row-1]][row-1] + w[row-1]
                result[col][row] = max(res, result[col][row-1])
    col, row, res = W, n, []
    while col > 0 and row > 0:# 从最后一项开始回溯,分最后一项被用上和最后一项没被用上两种情况讨论
        if result[col-w[row-1]][row-1] + w[row-1] > result[col][row-1]:
            res.append(w[row-1])
            col, row = col-w[row-1], row-1
        else:
            row -= 1

    return result[W][n], res# 返回最终得出的和,以及用上的数

def partition3(A):
    A.sort(reverse=True)#将A先从小到大排好,确保在DP中有多个解时优先返回含有较大数的那个解.
    # 例如A = [ 1, 1, 1, 2, 2, 2 ],理应返回1([1,2][1,2][1,2]),
    # 如果不排序会在第一个返回[1,1,1]导致最终返回0
    if sum(A) % 3 != 0: # 如果list不能被3整除,那他必然不能被分为和相等的三份
        return 0
    W = sum(A) // 3# 每份和的值必然为总和1/3
    res1, list1 = optimal_weight(W, A)
    if res1 != W:# 如果从这些数中凑不出和为W,那么直接返回0
        return 0
    for i in list1:# 如果从这些数中凑出和为W,那么去掉用过的数再看能不能从剩下的里面凑出来
        A.remove(i)
    res2, list2 = optimal_weight(W, A)
    if res2 != W:# 如果从这些数中凑不出和为W,那么直接返回0
        return 0
    return 1# 如果从这些数中凑出和为W,那么不用检查第三组,必然是可以的,直接返回1

```
- Q3:

```
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
```
