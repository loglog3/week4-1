import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def solve():
    N = int(input())
    row = [0]*N
    col = [0]*N
    dp = [[float('inf')]*N for _ in range(N)]

    for i in range(N):
        row[i], col[i] = map(int, input().split())
        dp[i][i] = 0
    for j in range(1, N):
        for start in range(N-j):

            end = start+j

            result = float('inf')
            for k in range(start, end):
                result = min(result,
                             dp[start][k]+dp[k+1][end] + row[start]*col[k]*col[end])

            dp[start][end] = result

    print(dp[0][-1])


solve()
# 5
# 10 13
# 13 12
# 12 13
# 13 10
# 10 12

# 4
# 1 3
# 3 2
# 2 3
# 3 1

# 8
# 1 100
# 100 1
# 1 100
# 100 1
# 1 100
# 100 1
# 1 100
# 100 1

# 6
# 2 1
# 1 2
# 2 3
# 3 4
# 4 3
# 3 2
