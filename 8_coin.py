import sys
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

coinType, target = list(map(int, read().rstrip().split()))
coin_list = []
for _ in range(coinType):
    coin_list.append(int(read()))

cnt = 0
for coinIdx in range(len(coin_list)-1, -1, -1):
    if coin_list[coinIdx] <= target and target!= 0:
        cnt += target//coin_list[coinIdx]
        rest = target % coin_list[coinIdx]
        target = rest
print(cnt)
