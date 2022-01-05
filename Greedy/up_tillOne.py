# n이 k의 배수 되도록 효율적으로 한 번에 빼기

n, k = map(int, input().split())
res = 0

while True:
    goal = (n // k) * k
    res += (n - goal)
    n = goal

    if n < k:
        break

    res += 1
    n //= k

res += (n-1)

print(res)
