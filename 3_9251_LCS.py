import sys
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

str1 = read().rstrip()
str2 = read().rstrip()

board = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

# for i in board:
#     print(i)
# print()

for r in range(1, len(str2)+1):
    for c in range(1, len(str1)+1):
        if str2[r-1] == str1[c-1]:
            board[r][c] = board[r-1][c-1] + 1
        else:
            board[r][c] = max(board[r-1][c], board[r][c-1])

# for i in board:
#     print(i)

print(board[-1][-1])
