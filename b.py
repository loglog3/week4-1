import sys
import itertools
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

cases = int(read())
peoples = []
mbties = []

for _ in range(cases):
    people = int(read())
    peoples.append(people)
    mbti = list(read().rstrip().split())
    mbties.append(mbti)

cnt = 0
cnts = []
ans = []
for case in range(cases):
    arr = mbties[case]
    nCr = itertools.combinations(arr, 3)
    for com in nCr:
        for i in range(2):
            for j in range(1, 3):
                for t in range(4):
                    if com[i][t] != com[j][t]:
                        cnt += 1
        cnts.append(cnt)
        cnt = 0
    # print(cnts)
    ans.append(min(cnts))
    cnts = []

for i in ans:
    print(i)
