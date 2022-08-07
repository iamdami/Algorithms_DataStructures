# n X m 크기의 금광
# 금광은 1 X 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어있음
# 채굴자는 첫 번째 열부터 출발해 금 캐기 시작
# 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있음
# 이후 m - 1번에 걸쳐 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 함
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기 출력하는 프로그램?

# 입력 조건
# 첫째 줄에 테스트 케이스 T 입력(1 <= T <= 1000)
# 매 테스트 케이스 첫째 줄에 n과 m니 공백으로 구분되어 입력됨(1 <= n, m <= 20)
# 둘째 줄에 n X m개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됨(1 <= 각 위치에 매장된 금의 개수 <= 100)

# 출력 조건
# 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기 출력
# 각 테스트 케이스는 줄 바꿈 이용해 구분

# 문제 해결
# 금광의 모든 위치에 대해 세 가지만 고려하면 됨
# 1. 왼쪽 위에서 오는 경우
# 2. 왼쪽 아래에서 오는 경우
# 3. 왼쪽에서 오는 경우
# 세 가지 중 가장 많은 금을 가지고 있는 경우를 테이블에 갱신해 문제 해결

# 테스트 케이스
for testcase in range(int(input())):
    # 금광 정보
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = []
    idx = 0

    for i in range(n):
        dp.append(arr[idx:idx+m])
        idx += m

    # 다이나믹 프로그래밍
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위
            if i == 0: leftUp = 0
            else: leftUp = dp[i - 1][j - 1] 
            # 왼쪽 아래
            if i == n - 1: leftDown = 0
            else: leftDown = dp[i + 1][j - 1]           
            # 왼쪽
            left =  dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(leftUp, leftDown, left)
    res = 0
    for i in range(n):
        res = max(res, dp[i][m - 1])
    print(res)
