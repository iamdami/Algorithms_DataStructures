Selection Sort
===
처리되지 않은 데이터 중 가장 작은 데이터 선택해 맨 앞에 있는 데이터와 바꾸는 것 반복  
<br>
N번 만큼 가장 작은 수 찾아 맨 앞으로 보내야 함  
구현 방식에 따라 사소한 오차는 있을 수 있지만 **O(N^2)**  
  
### Python
```
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):  # 선형 탐색 수행 -> 가장 작은 원소 찾기
        if array[min_index] > array[j]:  # 현재 가장 작은 원소보다 더 작은 원소가 있다면
            min_index = j  # 그 인덱스 값이 min_index에 저장되도록 함
    array[i], array[min_index] = array[min_index], array[i] # 가장 앞쪽 원소와 가장 작은 원소 서로 위치 스와프

print(array)
```
<br>

### C++
```
#include <bits/stdc++.h>

using namespace std;

int n = 10;  // 데이터 개수
int arr[10] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

int main(void) {
    for (int i = 0; i < n; i++) {
        int min_index = i; // 가장 작은 원소의 인덱스 
        for (int j = i + 1; j < n; j++) {
            if (arr[min_index] > arr[j]) {
                min_index = j;
            }
        }
        swap(arr[i], arr[min_index]); // 가장 앞쪽 원소와 가장 작은 원소 서로 위치 스와프
    }
    for(int i = 0; i < n; i++) {
        cout << arr[i] << ' ';
    }
}
```
<br>

### Java
```
import java.util.*;

public class Main {

    public static void main(String[] args) {

        int n = 10;
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

        for (int i = 0; i < n; i++) {
            int min_index = i; // 가장 작은 원소의 인덱스 
            for (int j = i + 1; j < n; j++) {
                if (arr[min_index] > arr[j]) {
                    min_index = j;
                }
            }
            // 가장 앞쪽 원소와 가장 작은 원소 서로 위치 스와프
            // 자바는 포인터 연산 지원하지 않기 때문에 temp 변수 사용해 값 기록, 변환
            int temp = arr[i];
            arr[i] = arr[min_index];
            arr[min_index] = temp;
        }

        for(int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
```
