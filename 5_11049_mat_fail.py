import sys
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

matrix_amount = int(read())
base = []
for _ in range(matrix_amount):
    a, b = map(int, read().rstrip().split())
    base.append([a, b, [a, b]])
# print(base)

total_cal = []

while len(base) > 1:
    tmp = 2**31
    for i in range(len(base)-1):
        cal = base[i][0]*base[i][1]*base[i+1][1]
        if cal == tmp:
            if (base[i][0] < tmpMin[0] or base[i+1][1] < tmpMin[1]) and (base[i][0]+base[i+1][1] < tmpMin[0]+tmpMin[1]):
                tmp = cal
                combine_idx = i
                tmpMin = [base[i][0], base[i+1][1]]
        elif cal < tmp:
            tmp = cal
            combine_idx = i
            tmpMin = [base[i][0], base[i+1][1]]
    total_cal.append(tmp)
    newBase = [base[combine_idx][0], base[combine_idx+1]
               [1], [base[combine_idx][0], base[combine_idx+1][1]]]
    del base[combine_idx]
    base[combine_idx] = newBase
    # print(base)


# print(base)
# print(total_cal)
ans = 0
for i in total_cal:
    ans += i

print(ans)
