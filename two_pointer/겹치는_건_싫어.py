import sys
from collections import defaultdict

input = sys.stdin.readline
if __name__ == '__main__':
	N, K = map(int, input().split())
	arr = list(map(int, input().split()))
	dup = defaultdict(int)

	a, b = 0, 0

	answer = 0
	while b < N:
		dup[arr[b]] += 1
		while dup[arr[b]] > K:
			dup[arr[a]] -= 1
			a += 1
		b += 1
		answer = max(answer, b - a)
	print(answer)