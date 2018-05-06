# Uses python3
import sys
def sort(L):
    # https://www.youtube.com/watch?v=gl_XQHTJ5hY
    for i in range(0,len(L)):
        for j in range(0,len(L)-1):
            if L[j]["r"]<L[j+1]["r"]:
                temp = L[j]
                L[j]=L[j+1]
                L[j+1]= temp
    return L
def get_optimal_value(capacity, weights, values):
    value = 0
    # write your code here
    list = []
    for i in range(0,len(weights)):
        list.append({"w":weights[i],"v":values[i],"r":values[i]/weights[i]})
    list = sort(list)
    for item in list:
        value += min(capacity,item["w"])*item["r"]
        capacity -= min(capacity,item["w"])
        if capacity == 0:
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

# print(get_optimal_value(10, [30],[500]))
# python fractional_knapsack.py
