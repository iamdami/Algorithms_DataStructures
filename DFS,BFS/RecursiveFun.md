재귀함수
===
자기 자신을 다시 호출하는 함수  
<br>

- 단순한 형태의 재귀 함수 예제  
```
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()
```
<br>

재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 함  
종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있음  
  
- 종료 조건 포함한 재귀 함수 예제  
```
def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)
```
<br>

- 재귀함수 이용 예제  
### 팩토리얼 구현 예제  
수학적으로 0!과 1!의 값은 1
```
# 반복적으로 구현한 n!
def factorial_iterative(n):        
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
       result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):        
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5) -> 실행결과 동일
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))
```
