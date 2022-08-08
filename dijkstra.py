from math import dist
import sys
input = sys.stdin.readline
INF =  int(1e9)  # 무한 의미하는 10억으로 설정  

# 노드 개수와 간선
node, edge = map(int, input().split())
# 시작 노드 번호
startNode = int(input())
# 각 노드에 연결되어 있는 노드 정보 담는 리스트
nodeInfoList = [[] for i in range(node + 1)]
# 방문한 적 있는지 체크하는 리스트
visited = [False] * (node + 1)
# 최단거리 테이블 모두 무한으로 초기화
distance = [INF] * (node + 1)

# 모든 간선 정보 입력받기
for _ in range(edge):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    nodeInfoList[a].append((b, c))

# 방문하지 않은 노드 중 가장 최단 거리 짧은 노드의 번호 반환
def getSmallestNode():
    minV = INF
    idx = 0  # 가장 최단 거리 짧은 노드 인덱스 
    for i in range(1, node + 1):
        if distance[i] < minV and not visited[i]:
            minV = distance[i]
            idx = 1
            return idx

def dijstra(startNode):
    # 시작노드 초기화
    distance[startNode] = 0
    visited[startNode] = True
    for j in nodeInfoList[startNode]:
        distance[j[0]] = j[1]
    # 시작 노드 제외한 전체 n - 1개 노드에 대해 반복 
    for i in range(node - 1):
        # 현재 최단 거리가 가장 짧은 노드 꺼내 방문 처리
        nowSmallest = getSmallestNode()
        visited[nowSmallest] =  True
        # 현재 노드와 연결된 다른 노드 확인
        for j in nodeInfoList[nowSmallest]:
            cost = distance[nowSmallest] + j[1]
            # 현재 노드 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijstra(startNode)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, node + 1):
    # 도달할 수 없는 경우 무한 출력
    if distance[i] == INF:
        print("INF")
    # 도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])
