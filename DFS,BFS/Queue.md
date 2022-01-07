Queue
===
먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조  
입구와 출구가 모두 뚫려 있는 터널 같은 형태  
  
- Python에서는 deque 라이브러리 사용  
  (기능적으로는 리스트로도 구현 가능하지만 시간복잡도가 더 높기 때문)  
- append(), popleft() 사용  
<br>

- cpp에서는 std 라이브러리 사용  
- push(), pop() 사용  
<br>
  
- java에서는 LinkedList<>내 구현되고 있는 큐(연결리스트로 구현된) 를 사용하는 게 일반적  
- offer(), poll() 사용  
  poll()은 원소를 단순히 꺼낼 뿐만 아니라 꺼내진 메서드를 바로 반환  

### python
```
from collections import deque 

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()  # 가장 왼쪽에 있는 원소 꺼낼 때 사용
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
# 먼저 들어온 순서대로 출력
# deque([3, 7, 1, 4])

queue.reverse() # 다음 출력을 위해 역순으로 바꾸기

print(queue) # 나중에 들어온 원소부터 출력
# deque(4, 1, 7, 3])
```
### cpp
```
#include <bits/stdc++.h>

using namespace std;

queue<int> q;

int main(void) {
    // 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
    q.push(5);
    q.push(2);
    q.push(3);
    q.push(7);
    q.pop();
    q.push(1);
    q.push(4);
    q.pop();
    // 먼저 들어온 원소부터 추출
    while (!q.empty()) {
        cout << q.front() << ' ';  
        // 가장 먼저 들어온 데이터 추출
        // 3 7 1 4
        
        q.pop();
    }
}
```
### Java
```
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Queue<Integer> q = new LinkedList<>();

        // 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
        q.offer(5);
        q.offer(2);
        q.offer(3);
        q.offer(7);
        q.poll();
        q.offer(1);
        q.offer(4);
        q.poll();
        // 먼저 들어온 원소부터 추출
        while (!q.isEmpty()) {
            System.out.println(q.poll());
        }
    }

}
```
