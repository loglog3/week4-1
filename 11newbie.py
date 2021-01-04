# 서류성적과 면접성적이 둘 중 하나는 최고여야한다.
# 서류 성적에 대해 정렬 서류 성적 1등은 무조건 합격
# 서류 성적 2등인 친구는 1등에 비해 면접 성적이 높아야한다.
# 면접성적이 더 낮으면 탈락, 더 높으면 면접성적에 대해서 현재 합격자 중 1등이 된다.
# 서류 성적 3등인 친구는 2등에 비해 면접 성적이 높아야한다.
# 즉 현재까지 면접 성적 1등보다 면접 성적이 높아야한다.

# 서류 및 면접 성적 배열 선언
# 합격자 카운트
# 최후 합격자 면접 성적(커트라인)
# 서류 성적 순으로 반복문을 돌리며 해당 지원자가 커트라인을 넘기면(등수가 더 낮으면) 카운트 더하기 일, 커트라인 갱신, 아니면 그냥 넘어가기

import sys
input = sys.stdin.readline


def solve():
    N = int(input())

    scores = [0]*(N+1)
    for _ in range(N):
        paper, interview = map(int, input().split())
        ####### 주목 #######
        scores[paper] = interview  # 이런식으로 score[paper] = interview 하니까.
        # paper로 sorting을 하지 않아도, 이미 sorting한 것과 같은 효과를 가져온다!!!

    cutline = scores[1]
    count = 1
    for i in range(2, N+1):
        if scores[i] < cutline:  # 등수가 낮아야 더 좋은 것
            count += 1
            cutline = scores[i]

    return str(count)


result = []
for _ in range(int(input())):
    result.append(solve())

print("\n".join(result))


# import sys
# sys.stdin = open('input.txt', 'r')
# read = sys.stdin.readline

# testcase = int(read())
# ans = []
# while testcase != 0:
#     newbie = int(read().rstrip())
#     scorelist = []

#     for i in range(newbie):
#         scorelist.append(list(map(int, read().rstrip().split())))
#     scorelist.sort(key=lambda x: (x[0], x[1]))

#     # for i in scorelist:
#     #     print(i)
#     can = []
#     maxCan = []

#     can = []
#     can.append(scorelist[0])
#     bound = scorelist[0][1]
#     for i in range(1, len(scorelist)):
#         if scorelist[i][1] > bound:
#             continue
#         else:
#             can.append(scorelist[i])
#             bound = scorelist[i][1]
#     # print('can', can)
#     if len(can) > len(maxCan):
#         maxCan = can
#     ans.append(len(maxCan))
#     testcase -= 1


# print('\n'.join(map(str, ans)))
