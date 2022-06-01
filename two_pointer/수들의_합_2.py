import sys

input = sys.stdin.readline


if __name__ == '__main__':
	N, M = map(int, input().split())
	A = list(map(int, input().split()))
	l, r = 0, 0
	total = A[0]
	answer = 0

	while True:
		if total <= M:
			if total == M:
				answer += 1
			r += 1
			if r == N:
				break
			total += A[r]
		else:
			total -= A[l]
			l += 1

	print(answer)
