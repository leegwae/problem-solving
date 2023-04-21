# k진수에서 소수 개수 구하기

https://school.programmers.co.kr/learn/courses/30/lessons/92335



## 문제

`n`을 `k`진수로 바꾸었을 때 아래 조건에 맞는 소수가 몇 개인가?

- `0P0`처럼 소수 양쪽에 0이 있음
- `P0`처럼 소수 오른쪽에만 0이 있음
- `0P`처럼 소수 왼쪽에만 0이 있음
- `P`처럼 소수 양쪽에 아무것도 없음
- (단, `P`는 각 자릿수에 0을 포함하지 않는다)



## 아이디어

1. `n`을 `k`진수로 바꾼다.
2. 0을 기준으로 자르면서 현재까지 모인 수가 소수인지 구한다.



## 풀이

```python
def isPrime(decimal):
    if decimal <= 1:
        return False
    
    for i in range(2, decimal):
        if decimal % i == 0:
            return False
        
    return True
```

소수 판별 알고리즘으로 `O(n)`을 돌리면 시간 초과난다. 최적화된 소수 판별 알고리즘을 사용한다.

```python
def convert(decimal, base):
    converted = ''
    
    몫 = decimal
    
    while 몫 > 0:
        converted = str(몫 % base) + converted
        몫 //= base
    
    return converted

def isPrime(decimal):
    if decimal <= 1:
        return False
    
    i = 2
    while i * i <= decimal:
        if decimal % i == 0:
            return False
        i += 1
    return True

def solution(n, k):
    answer = 0

    s = convert(n, k)
    idx = 0
    p = ''
    while idx < len(s):
        if s[idx] == '0':
            if len(p) > 0:
                if isPrime(int(p)):
                    answer += 1
                p = ''
        else:
            p += s[idx]
        idx += 1
        
    if len(p) > 0 and isPrime(int(p)):
        answer += 1
    
    return answer
```

