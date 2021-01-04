
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10000)
# INF = sys.maxsize
INF = 99
n = int(input())
mat = [list(map(int, input().split()))for _ in range(n)]
# dp = [[INF]*(1 << n)for _ in range(n)]
# 1<<4 == 16
dp = [[INF]*(1 << n)for _ in range(n)]
# print(dp)
for i in dp:
    print(i)
# print(mat)


def dfs(current, visit):
    # 모든 도시를 다 방문했따. 돌아가면 된다 이제,
    if visit == (1 << n)-1:
        # 처음위치인 0번도시로 갈 수 없다면
        if mat[current][0] == 0:
            return INF
        else:
          # 첫 도시로 돌아가기!, currnet에서 0번 도시로 가는 비용 리턴,
            return mat[current][0]
    # 이미 방문했던 곳이라면, 값을 그대로 리턴
    if dp[current][visit] != INF:
        print('현위치', current, '기방문', bin(visit))
        return dp[current][visit]
    for i in range(1, n):
        # 방문하지 않았고, 비용이 0이 아니면
        # for j in dp:
        #     print(j)
        if not visit & (1 << i) and mat[current][i] != 0:
            # dp[현재도시][방문지] = min(현재최소, dfs들어가서 나오는 최소)
            # n은 도시 수,
            # i를 방문했다는 의미에서 1<<i
            dp[current][visit] = min(dp[current][visit], dfs(
                i, visit | (1 << i))+mat[current][i])
    return dp[current][visit]


# DFS는 끊임없이 비용을 리턴한다
# DP는 row 현위치, col 방문한곳의 table형태로, 그 순간의 최소비용을 저장하고 있다.
# mat은 단순 이동시의 비용을 보관하고 있다
# 현재도시, 방문지(1이기때문에 0번도시 방문한 것.).
print(dfs(0, 1))

for i in dp:
    print(i)
