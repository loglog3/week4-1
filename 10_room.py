import sys
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

meeting_amount = int(read())

meeting_list = []
for i in range(meeting_amount):
    meeting_list.append(list(map(int, read().rstrip().split())))
# print(meeting_list)

meeting_list.sort(key=lambda x: (x[1], x[0]))
# for i in meeting_list:
#     print(i)

possible = []
possible.append(meeting_list[0])
for i in range(1, len(meeting_list)):
    if possible[-1][-1] <= meeting_list[i][0]:
        possible.append(meeting_list[i])

# for i in possible:
#     print(i)

print(len(possible))
