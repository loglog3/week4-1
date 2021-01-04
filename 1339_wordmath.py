import sys
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

n = int(read())
arr = []
for i in range(n):
    arr.append(read().rstrip())

print(arr)
arr.sort(key=len)
arr.reverse()
print(arr)

converter = {}
number = 9
for i in arr:
    for j in range(len(i)):
        if i[j] not in converter:
            converter[i[j]] = number
            number -= 1

print(converter)
