# 반복되는 수열 계산해 적용


n, m, k = map(int, input().split())
numList = list(map(int, input().split()))

numList.sort()

first = numList[n-1]
second = numList[n-2]

# 가장 큰 수 더해지는 횟수 계산
cnt = int(m / (k + 1)) * k
cnt += m % (k + 1)

res = 0

res += cnt * first
res += (m-cnt) * second

print(res)
