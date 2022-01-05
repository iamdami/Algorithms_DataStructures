# 각 행마다 가장 작은 수 찾은 후 그 수 중 가장 큰 수 찾기


n, m = map(int, input().split())

res = 0

for i in range(n):
    cardList = list(map(int, input().split()))
    minNum = min(cardList)
    res = max(res, minNum)

print(res)
