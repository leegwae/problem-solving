# A와_B

https://www.acmicpc.net/problem/12904

## 문제

- 문자열 T, S가 주어진다. 
- 문자열 S에 다음 연산을 사용할 수 있다.
  - 문자열 뒤에 A를 추가한다.
  - 문자열을 뒤집고 뒤에 B를 추가한다.
- 문자열 S를 T로 만들 수 있을까?

## 아이디어: 백트래킹

- S를 T의 길이만큼의 문자열을 만드려면 T-S만큼 연산을 실행해야한다.
- 그러므로 2^(T-S)만큼의 경우의 수를 살피면 된다.

```python
import sys

input = sys.stdin.readline


def f(s: str):
	if len(s) == len(T):
		if s == T:
			print(1)
			exit(0)
		return

	f(s+'A')
	f(s[::-1]+'B')


if __name__ == '__main__':
	S = input().strip()
	T = input().strip()

	f(S)
	print(0)
```

- 하지만 백트래킹은 시간 초과가 난다. 

## 해결: 그리디 알고리즘

- B를 A로 만드는 그리디 알고리즘으로 바꿔서 경우의 수를 좁혀보자.
- B에 두 가지 연산을 수행할 수 있다.
  - 문자열 뒤에서 A를 뺀다: B[-1]이 A여야한다.
  - 문자열 뒤에서 B를 빼고 문자열을 뒤집는다: B[-1]이 A여야한다.
- 따라서, 매번 한 가지 연산만이 가능하다.

=> O(B-A)로 시간복잡도를 개선할 수 있다.

```python
import sys

input = sys.stdin.readline


def f(t: str):
	if len(t) == len(S):
		if t == S:
			print(1)
			exit(0)
		return

	if t[-1] == 'A':
		f(t[:-1])

	if t[-1] == 'B':
		f(t[:-1][::-1])


if __name__ == '__main__':
	S = input().strip()
	T = input().strip()

	f(T)
	print(0)
```