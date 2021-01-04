import sys
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


tree = {}
nodes = int(read())
basic = []
# [부모, 자식, 가중치]


def solve():
    for _ in range(nodes-1):
        parent, child, weight = map(int, read().rstrip().split())
        basic.append([parent, child, weight])

    dp = [[0] for _ in range(nodes+1)]

    for i in range(len(basic)-1, -1, -1):
        parent = basic[i][0]
        weight = basic[i][2]
        child = basic[i][1]
        newNum = max(dp[child]) + weight
        dp[parent].append(newNum)
        # dp[parent].append(weight)

    candidate = []
    for i in dp:
        if len(i) >= 2:
            i.sort(reverse=True)
            sum = i[0] + i[1]
            candidate.append(sum)

    print(basic)
    print(dp)
    print(max(candidate))


if nodes == 1:
    print(0)
else:
    solve()

# 1시간 25분
