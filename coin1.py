import sys
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

coins, target = list(map(int, read().rstrip().split()))

coin_list = []
for _ in range(coins):
    coin_list.append(int(read()))

dp = [0 for _ in range(target+1)]
dp[0] = 1
for i in range(target+1):
    for coin in range(coins):
        dp[i] = max(dp[i], dp[i] + dp[i-coin_list[coin]])

print(dp[-1])
