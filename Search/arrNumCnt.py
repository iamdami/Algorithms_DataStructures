# 정렬된 배열에서 특정 수의 개수 구하기
# N개의 원소 포함하고 있는 수열이 오름차순으로 정렬돼있음
# 이때 이 수열에서 x가 등장하는 횟수 계산
# 예) 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소 4개 -> 4 출력
# 시간복잡도 O(logN)으로 알고리즘 설계하지 않으면 시간 초과 판정

# 입력 조건
# 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됨
# (1 <= N <= 1,000,000), (-10^9 <= x <= 10^9)
# 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됨
# (-10^9 <= 각 원소의 값 <= 10^9)

# 출력 조건
# 수열의 원소 중 값이 x인 원소 개수 출력
# 단, 값이 x인 원소가 하나도 없다면 -1 출력

# 입력 예시
# 7 2
# 1 1 2 2 2 2 3

# 출력 예시
# 4


# 시간복잡도 O(logN)으로 동작하는 알고리즘 요구
# 일반적인 선형 탐색으로는 시간 초과 판정
# 데이터가 정렬되어 있기 때문에 이진 탐색 가능
# 특정 값 등장하는 첫 번째 위치와 마지막 위치 찾아 차이 계산해 문제 해결 가능


from bisect import bisect_left, bisect_right

def countByRange(a, leftV, rightV):
    rightIdx =  bisect_right(a, rightV)
    leftIdx = bisect_left(a, leftV)
    return rightIdx - leftIdx

n, x = map(int, input().split())
arr = list(map(int, input().split()))

# 값이 [x, x] 범위에 있는 데이터 개수 계산
cnt = countByRange(arr, x, x)

# 값이 x인 원소 존재하지 않으면
if cnt == 0:
    print(-1)
# 값이 x인 원소 존재하면
else:
    print(cnt)