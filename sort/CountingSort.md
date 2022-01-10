Counting Sort(계수 정렬)
===
- 특정 조건 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘  
  - 데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능  
데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 O(N+K) 보장  
<br>

- 계수 정렬의 시간 복잡도, 공간 복잡도: **O(N+K)**
데이터 개수만큼 cnt값 체크함 O(N)  
데이터 중 가장 큰 값을 의미하는 K만큼 각 인덱스 확인하며,  
그 인덱스에 기록되어 있는 값 만큼 출력  
  
- 계수 정렬은 때에 따라 심각한 비효율성 초래할 수 있음  
  - 데이터가 0과 999,999로 단 2개만 존재하는 경우  
  
- 계수 정렬은 동일한 값 가지는 데이터가 여러 개 등장할 때 효과적으로 사용 가능  
  - 성적의 경우!  
<br>

### Python
```
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
        # 이 이중 반복문의 시간 복잡도는 N+K
```
<br>

### C++
```
#include <bits/stdc++.h>
#define MAX_VALUE 9

using namespace std;

int n = 15;
// 모든 원소의 값이 0보다 크거나 같다고 가정
int arr[15] = {7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};
// 모든 범위를 포함하는 배열 선언(모든 값은 0으로 초기화)
int cnt[MAX_VALUE + 1];

int main(void) {
    for (int i = 0; i < n; i++) {
        cnt[arr[i]] += 1; // 각 데이터에 해당하는 인덱스의 값 증가
    }
    for (int i = 0; i <= MAX_VALUE; i++) { // 배열에 기록된 정렬 정보 확인
        for (int j = 0; j < cnt[i]; j++) {
            cout << i << ' '; // 띄어쓰기를 기준으로 등장한 횟수만큼 인덱스 출력
        }
    }
}
```
<br>

### Java
```
import java.util.*;

public class Main {
	
    public static final int MAX_VALUE = 9;

    public static void main(String[] args) {
    	
        int n = 15;
        // 모든 원소의 값이 0보다 크거나 같다고 가정
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};
        // 모든 범위를 포함하는 배열 선언(모든 값은 0으로 초기화)
        int[] cnt = new int[MAX_VALUE + 1];

        for (int i = 0; i < n; i++) {
            cnt[arr[i]] += 1; // 각 데이터에 해당하는 인덱스의 값 증가
        }
        for (int i = 0; i <= MAX_VALUE; i++) { // 배열에 기록된 정렬 정보 확인
            for (int j = 0; j < cnt[i]; j++) {
                System.out.print(i + " "); // 띄어쓰기를 기준으로 등장한 횟수만큼 인덱스 출력
            }
        }
    }

}
```
