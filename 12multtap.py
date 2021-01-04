# 먼저 생각하기
# 일단 꽂는다
# 먼저 다시 사용하는건 계속 꽂아놓고, 그렇지 않은 걸 뺀다
# 3구 이상이면, 계속 살펴보면서, 먼저 나오는 애들은 저장해놓는다.
# n-1구 까지 저장하고 나면, 해당없는 걸 빼버린다.
# 3구짜리면, 앞으로 사용할 두개만 저장해놓고, 하나는 빼버린다.
# 리스트를 하나씩 순회한다.
# 더 이상 뒤에 연결할 것들이 없으면, 아무거나 뽑으면 된다.

import sys
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

hole, appliance = map(int, read().rstrip().split())
plugged = []

sequence = read().rstrip().split()
cnt = 0
f = -1
if hole >= appliance:
    print(0)
else:
    while len(plugged) != hole:
        f += 1
        if sequence[f] in plugged:
            continue
        else:
            plugged.append(sequence[f])
    for i in range(hole, appliance):
        soon = []
        if sequence[i] in plugged:
            continue
        else:
            for j in range(i, appliance):
                if sequence[j] in plugged and sequence[j] not in soon:
                    if len(soon) >= hole-1:
                        break
                    soon.append(sequence[j])
                    # print('soon', soon)
            for unplug in plugged:
                if unplug not in soon:
                    plugged.remove(unplug)
                    cnt += 1
                    break
            plugged.append(sequence[i])
            # print('plugged', plugged)
    print(cnt)


'''
testcase 모음

2 7
2 3 2 3 1 2 7
답: 2

2 5
5 2 2 3 5
답: 1

2 4
5 3 1 5
답: 1

3 6
1 1 1 1 2 3
답: 0

3 8
1 2 3 4 1 1 1 2
답: 1

2 15
3 2 1 2 1 2 1 2 1 3 3 3 3 3 3
답: 2

1 3
1 2 1
답: 2

3 14
1 4 3 2 5 4 3 2 5 3 4 2 3 4
답 4

3 11
11 8 11 7 2 8 2 7 5 10 2
답 3

'''
