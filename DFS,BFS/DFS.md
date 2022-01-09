DFS
===
**깊이 우선 탐색**  
그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘  
스택 자료 구조(혹은 재귀함수) 이용  
- 구체적 동작 과정  
1. 탐색 시작 노드 스택에 삽입하고 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리  
   방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드 꺼냄  
3. 더 이상 2번 과정 수행할 수 없을 때까지 반복  
  
### Python  
```
# DFS 함수 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')  # 노드 방문했다는 의미로 해당 노드 출력
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:  # 인접 노드가 방문되지 않은 상태라면 그 노드에 대해 재귀함수 이용해 방문
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],  # 그래프 초기화
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9  
# 처음엔 모든 노드를 하나도 방문하지 않은 것처럼 초기화
# 인덱스 0은 사용하지 않기 위해 일부러 하나도 큰 크기(9)로 초기화

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```
<br>

# C++
```
#include <bits/stdc++.h>

using namespace std;

bool visited[9];
vector<int> graph[9];

// DFS 함수 정의
void dfs(int x) {
    // 현재 노드를 방문 처리
    visited[x] = true;
    cout << x << ' ';
    // 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for (int i = 0; i < graph[x].size(); i++) {
        int y = graph[x][i];
        if (!visited[y]) dfs(y);  // 인접 노드가 방문되지 않은 상태라면 그 노드에 대해 재귀함수 이용해 방문
        }
    }
}

int main(void) {
    // 노드 1에 연결된 노드 정보 저장 
    graph[1].push_back(2);
    graph[1].push_back(3);
    graph[1].push_back(8);
    
    // 노드 2에 연결된 노드 정보 저장 
    graph[2].push_back(1);
    graph[2].push_back(7);
    
    // 노드 3에 연결된 노드 정보 저장 
    graph[3].push_back(1);
    graph[3].push_back(4);
    graph[3].push_back(5);
    
    // 노드 4에 연결된 노드 정보 저장 
    graph[4].push_back(3);
    graph[4].push_back(5);
    
    // 노드 5에 연결된 노드 정보 저장 
    graph[5].push_back(3);
    graph[5].push_back(4);
    
    // 노드 6에 연결된 노드 정보 저장 
    graph[6].push_back(7);
    
    // 노드 7에 연결된 노드 정보 저장 
    graph[7].push_back(2);
    graph[7].push_back(6);
    graph[7].push_back(8);
    
    // 노드 8에 연결된 노드 정보 저장 
    graph[8].push_back(1);
    graph[8].push_back(7);
    
    dfs(1);
}
```
<br>

### Java
```
import java.util.*;

public class Main {

    public static boolean[] visited = new boolean[9];  // 방문처리 위해 불리언 객체 9개 포함하는 리스트
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
    // 2D List 대신 Array List 중첩해 사용
    // Array List는 특정 요소 접근하는데 상수 시간이 소요되기에 2D List보다 효과적

    // DFS 함수 정의
    public static void dfs(int x) {
        // 현재 노드를 방문 처리
        visited[x] = true;
        System.out.print(x + " ");
        // 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for (int i = 0; i < graph.get(x).size(); i++) {
            int y = graph.get(x).get(i);
            if (!visited[y]) dfs(y);  // 인접 노드가 방문되지 않은 상태라면 그 노드에 대해 재귀함수 이용해 방문
        }
    }

    public static void main(String[] args) {
        // 그래프 초기화
        for (int i = 0; i < 9; i++) {
            graph.add(new ArrayList<Integer>());
        }

        // 노드 1에 연결된 노드 정보 저장 
        graph.get(1).add(2);
        graph.get(1).add(3);
        graph.get(1).add(8);
        
        // 노드 2에 연결된 노드 정보 저장 
        graph.get(2).add(1);
        graph.get(2).add(7);
        
        // 노드 3에 연결된 노드 정보 저장 
        graph.get(3).add(1);
        graph.get(3).add(4);
        graph.get(3).add(5);
        
        // 노드 4에 연결된 노드 정보 저장 
        graph.get(4).add(3);
        graph.get(4).add(5);
        
        // 노드 5에 연결된 노드 정보 저장 
        graph.get(5).add(3);
        graph.get(5).add(4);
        
        // 노드 6에 연결된 노드 정보 저장 
        graph.get(6).add(7);
        
        // 노드 7에 연결된 노드 정보 저장 
        graph.get(7).add(2);
        graph.get(7).add(6);
        graph.get(7).add(8);
        
        // 노드 8에 연결된 노드 정보 저장 
        graph.get(8).add(1);
        graph.get(8).add(7);

        dfs(1);
    }

}
```
<br>
