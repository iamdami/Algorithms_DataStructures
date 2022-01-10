Quick Sort
===
기준 데이터 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치 바꾸는 방법  
일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘  
병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 됨  
가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정  
  
피벗을 기준으로 데이터 묶음 나누는 작업을 분할(Divide)이라고 함  
- 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 **O(NlogN)**  
- 최악의 경우 O(N^2)  
  - 첫 번째 원소를 피벗으로 삼을 때, 이미 정렬된 배열에 대해 퀵 정렬 수행시!
<br>

### Python  
```
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):  # 선형탐색
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]):
            left += 1  # left는 항상 오른쪽으로
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1  # right는 항상 왼쪽으로
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    # 이상적인 경우 왼쪽과 오른쪽이 서로 균형있게 분할 이루어짐

quick_sort(array, 0, len(array) - 1)
print(array)
```
<br>

### Python 장점 살린 방식
-Using List slicing and List comprehension
```
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    # 피벗 제외한 리스트 원소 하나씩 확인-> 피벗값보다 작은 값의 원소는 피벗 왼쪽으로
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    # 피벗 제외한 리스트 원소 하나씩 확인-> 피벗값보다 큰 값의 원소는 피벗 오른쪽으로
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    # [왼쪽 부분 + 피벗 부분 + 오른쪽 부분]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```
<br>

### C++ 
```
#include <bits/stdc++.h>

using namespace std;

int n = 10;
int arr[10] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

void quickSort(int* arr, int start, int end) {
    if (start >= end) return; // 원소가 1개인 경우 종료
    int pivot = start; // 피벗은 첫 번째 원소
    int left = start + 1;
    int right = end;
    while (left <= right) {
        // 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end && arr[left] <= arr[pivot]) left++;
        // 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start && arr[right] >= arr[pivot]) right--;
        // 엇갈렸다면 작은 데이터와 피벗을 교체
        if (left > right) swap(arr[pivot], arr[right]);
        // 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else swap(arr[left], arr[right]);
    }
    // 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quickSort(arr, start, right - 1);
    quickSort(arr, right + 1, end);
}

int main(void) {
    quickSort(arr, 0, n - 1);
    for (int i = 0; i < n; i++) {
        cout << arr[i] << ' ';
    }
}
```
<br>

### Java
```
import java.util.*;

public class Main {

    public static void quickSort(int[] arr, int start, int end) {
        if (start >= end) return; // 원소가 1개인 경우 종료
        int pivot = start; // 피벗은 첫 번째 원소
        int left = start + 1;
        int right = end;
        while (left <= right) {
            // 피벗보다 큰 데이터를 찾을 때까지 반복
            while (left <= end && arr[left] <= arr[pivot]) left++;
            // 피벗보다 작은 데이터를 찾을 때까지 반복
            while (right > start && arr[right] >= arr[pivot]) right--;
            // 엇갈렸다면 작은 데이터와 피벗을 교체
            if (left > right) {
                int temp = arr[pivot];
                arr[pivot] = arr[right];
                arr[right] = temp;
            }
            // 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            else {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
            }
        }
        // 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행(재귀적 호출)
        quickSort(arr, start, right - 1);
        quickSort(arr, right + 1, end);
    }

    public static void main(String[] args) {
        int n = 10;
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

        quickSort(arr, 0, n - 1);

        for(int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }

}
```
