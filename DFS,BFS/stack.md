stack
===
먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조  
입구와 출구가 동일한 형태  
  
- 파이썬에서는 다른 표준 라이브러리 없이 리스트 자료형 이용  
- append(), pop() 활용  
<br>

- cpp에서는 std 라이브러리 이용
- push(), pop() 활용
- 최상단 원소 확인시 top()  
<br>

- java에서는 push(), pop() 활용
- 최상단 원소 확인시 peek()  
  
### python
```
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
# 최하단 원소부터 출력
# [1, 3, 2, 5]

print(stack[::-1])
# 최상단 원소부터 출력
# [5, 2, 3, 1]
```
  
### cpp
```
#include <bits/stdc++.h>

using namespace std;

stack<int> s;

int main(void) {
    // 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
    s.push(5);
    s.push(2);
    s.push(3);
    s.push(7);
    s.pop();
    s.push(1);
    s.push(4);
    s.pop();
    // 스택의 최상단 원소부터 출력
    while (!s.empty()) {
        cout << s.top() << ' ';
        // top(): 현재 최상단 원소가 무엇인지?
        s.pop(); // 1, 3, 2, 5
    }
}
```
### Java
```
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();

        // 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
        s.push(5);
        s.push(2);
        s.push(3);
        s.push(7);
        s.pop();
        s.push(1);
        s.push(4);
        s.pop();
        // 스택의 최상단 원소부터 출력
        while (!s.empty()) {
            System.out.println(s.peek());
            s.pop();  // 1, 3, 2, 5
        }
    }

}
```
