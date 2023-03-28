# ZOAC

https://www.acmicpc.net/problem/16719

## 문제

- 문자열이 주어진다.
- 아직 보여주지 않은 문자 중 추가했을 때의 문자열이 사전 순으로 가장 앞에 오도록 하는 문자를 보여준다.

```
예) STARTLINK

A
AI
AIK
AINK
ALINK
ARLINK
ARTLINK
SARTLINK
STARTLINK
```

## 아이디어

분할-정복 알고리즘으로 풀 수 있다.

1. 문자열에서 가장 작은 문자를 찾는다.
2. 보여줄 문자열에 추가하고 출력한다.
3. 해당 문자를 기준으로 문자열을 오른쪽, 왼쪽으로 나눈다.
4. 왼쪽 문자열에 대해 1번부터 5번까지 진행
5. 오른쪽 문자열에 대해 1번부터 5번까지 진행