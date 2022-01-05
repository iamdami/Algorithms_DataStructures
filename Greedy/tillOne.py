# 최대한 많이 나누고 n-1 수행하기


n, k = map(int, input().split())
res = 0

while n >= k:
    while n % k != 0:
        n -= 1
        res += 1
    n //= k
    res += 1

while n > 1:
    n -= 1
    res += 1

print(res)
