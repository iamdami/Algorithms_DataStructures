# n 입력 받고 00시 00분 00초 ~ n시 59분 59초까지 3이 한 번이라도 포함되면 cnt
# n 입력 받고 시, 분, 초 단위는 3중 for문으로 구성, if문에서 문자열로 합쳐서 그 문자열에 3 포함되면 cnt 증가

n = int(input())

cnt = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                cnt += 1
print(cnt)
