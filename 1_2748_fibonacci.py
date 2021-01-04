import sys
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

fibo = int(read())

dp = [0, 1] + [0] * (fibo-1)

for i in range(2, fibo+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[fibo])
# print(dp)