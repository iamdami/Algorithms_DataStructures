'''
N*M 크기의 미로
여러 마리 괴물 피해 탈출하기
캐릭터 위치: (1, 1)
출구: (N, M)
한 번에 한 칸씩 이동 가능
괴물 있는 부분: 0
괴물 없는 부분: 1

Q. 탈출 위해 움직여야 하는 최소 칸의 개수?
  (칸 셀 때는 시작 칸과 마지막 칸 포함해 계산)
'''

# BFS 이용
# 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드 탐색
# 상, 하, 좌, 우로 연결된 모든 노드로의 거리가 1로 동일
# (1, 1) 지점부터 BFS 수행해 모든 노드의 최단 거리 값 기록해 해결 가능

# 1. 처음에 (1, 1)에서 시작
# 2. (1, 1) 좌표에서 상, 하, 좌, 우로 탐색해 방문 가능한 위치의 노드를 방문하고, 새롭게 방문하는 노드의 값을 2로 바꿈
# 3. 이런 식으로 BFS를 계속 수행하면 결과적으로 최단 경로 값들이 1씩 증가하는 형태로 변경됨 

from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1  # 직전 노드에 +1한 값 저장
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))
