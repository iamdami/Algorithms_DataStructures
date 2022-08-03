from bisect import bisect_left, bisect_right

def countByRange(a, leftV, rightV):
    rightIdx =  bisect_right(a, rightV)
    leftIdx = bisect_left(a, leftV)
    return rightIdx - leftIdx

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(countByRange(a, 3, 3))  # 값이 3인 데이터 개수 출력
print(countByRange(a, -1, 3))  # 값이 [-1, 3]범위에 있는 데이터 개수 출력
