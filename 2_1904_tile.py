import sys
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

fibo = int(read())


dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 3

if fibo >= 4:
    for i in range(3, fibo+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746


print(dp[fibo])
# print(dp)
