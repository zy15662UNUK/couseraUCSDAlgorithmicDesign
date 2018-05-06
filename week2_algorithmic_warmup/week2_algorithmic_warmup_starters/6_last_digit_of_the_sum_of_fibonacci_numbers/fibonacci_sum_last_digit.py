# Uses python3
import sys
# sigma(Fn) = Fn+2 -1
# Fn+2 % 10 obtained from Pisano period.
# (Fn+2 -1)%10 = Fn+2 % 10 -1 if it > 0, else (Fn+2 -1)%10 =9
def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    string = "011235831459437077415617853819099875279651673033695493257291"#Pisano period. for mod 10
    result=int(string[(n+2)%60])-1
    if result >= 0:
        return result
    else:
        return 9

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
# print(fibonacci_sum_naive(832564823476))
# python fibonacci_sum_last_digit.py
