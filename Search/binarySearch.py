def binarySearch(arr, targetm start, end):
  if start > end:
    return None
  mid = (start + end) // 2  # start + end 에서 2를 나눈 몫  
  if arr[mid] == target:
    return mid  # 찾은 경우 중간점 인덱스 반환  
  elif arr[mid] > target:
    return binarySearch(arr, target, start, mid - 1)  # 중간점 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  else:
    return binary_search(arr, target, mid + 1, end)  # 중간점 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인  
  
n, target = list(map(int, input(), split()))  # 원소 개수와 찾고자 하는 값 입력 받기
arr = list(map(int, input().split()))  # 전체 원소 입력 받기

res = binarySearch(arr, target, 0, n - 1)
if res == None:
  print("원소가 존재하지 않음")
else:
  print(result + 1)

  
