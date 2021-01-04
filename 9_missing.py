import sys
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

a = read().split('-')
s = 0
for i in a[0].split('+'):
    s += int(i)
print(s)
for i in a[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)

# equation = read()
# # print(equation)
# equation = equation.split('-')
# # print(equation)
# for i in range(len(equation)):
#     equation[i] = equation[i].split('+')
#     for j in range(len(equation[i])):
#         equation[i][j] = int(equation[i][j])
# # print(equation)

# total = 0
# for i in range(len(equation)):
#     eachsum = 0
#     for j in range(len(equation[i])):
#         eachsum += equation[i][j]
#     equation[i] = eachsum
#     if i == 0:
#         # total += equation[i]
#         total += eachsum
#     else:
#         total -= eachsum
# print(total)
