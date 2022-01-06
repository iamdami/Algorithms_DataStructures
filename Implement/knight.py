# 나이트 위치 입력 받기
# 나이트 이동 방향 정의
# 해당 경우의 수에 대해 이동 가능한지 파악
# 해당 위치 이동 가능하면 cnt 증가

current_knight = input()
col = int(ord(current_knight[0])) - int(ord('a')) + 1
row = int(current_knight[1])

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]  # 8가지 경우의 수

res = 0
for step in steps:
    nxt_col = col + step[1]
    nxt_row = row + step[0]

    if 1 <= nxt_col <= 8 and 1 <= nxt_row <= 8:
        res += 1

print(res)
