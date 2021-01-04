# 시간복잡도 O(NM)이 필요하지만, 공간은 NM이 필요하진  않은 방법
# 가방에서 직접 꺼내서 쓰면 된다. 전 단계의 최적해들을 table로 관리하는게 아니라 실시간 업데이트 해준다

import sys
sys.stdin = open('input.txt', 'r')

read = sys.stdin.readline
items, packSize = map(int, read().split())
bag = [tuple(map(int, read().split())) for _ in range(items)]

dp = [0 for _ in range(packSize+1)]

for item in range(items):
    for size in range(packSize, 1, -1):
        if bag[item][0] <= size:
            dp[size] = max(
                dp[size], dp[size-bag[item][0]] + bag[item][1])

print('bag', bag)
print('dp', dp)
print(dp[-1])
