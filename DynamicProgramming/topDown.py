# 한 번 계산된 결과는 메모이제이션하기 위해 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(탑다운)
def fibo(x):
    # 종료 조건(1 혹은 2일 때 1 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제면 점화식에 따라 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))