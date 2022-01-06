# 상하좌우 문제

n = int(input())
plans = input().split()

x, y = 1, 1
plan = 0
i = 0
nx = 0
ny = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moveType = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(moveType)):
        if plan == moveType[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
