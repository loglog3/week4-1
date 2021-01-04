import sys
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

board = [[0 for _ in range(len(str1))] for _ in range(len(str2))]
base.sort(key=lambda x: (x[0], x[1]))

INF = sys.maxsize

print('\n'.join(map(str, ans)))

split은 str를 list로 바꾼다.