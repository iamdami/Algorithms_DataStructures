# 입력값 중 가장 큰 수와 두번째로 큰 수 저장
# 가장 큰 수 k번 더하고 두번째 큰 수 한 번 더하는 연산 반복


n, m, k = map(int, input().split())
numList = list(map(int, input().split()))

numList.sort()

first = numList[n-1]
second = numList[n-2]

res = 0

while True:
    for i in range(k):
        if m == 0:
            break
        res += first
        m -= 1
    if m == 0:
        break
    res += second
    m -= 1

print(res)
