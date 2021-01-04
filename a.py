import sys
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

num = read()
word_list = list(read().split())

# print(word_list)
b = True
if len(num) == 1:
    print(1)
else:
    for i in range(len(word_list)-1):
        for j in range(i+1, len(word_list)):
            if word_list[i][-1] == word_list[j][0]:
                b = True
            elif word_list[i][0] == word_list[j][-1]:
                b = True
            else:
                b = False
                break
        if b == False:
            break

    if b == True:
        print(1)
    else:
        print(0)
