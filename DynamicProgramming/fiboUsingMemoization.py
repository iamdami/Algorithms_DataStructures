# 메모이제이션 이용하면 피보나치 수열 함수의 시간 복잡도는 O(N)

d = [0] * 100

def fibo(x):
    print(f"f({str(x)})", end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

fibo(6)