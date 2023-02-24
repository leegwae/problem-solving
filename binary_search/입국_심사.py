import sys

input = sys.stdin.readline

if __name__ == '__main__':
	# N: 심사대 수, M: 사람 수
	N, M = map(int, input().split())
	T = [int(input()) for _ in range(N)]

	# t초까지 심사대 T[i]가 심사를 완료한 사람 수는 t // T
	left, right = min(T) * (M // N), max(T) * (M // N)
	while left <= right:
		mid = (left + right) // 2

		c = 0
		for i in range(N):
			c += (mid // T[i])

		if c >= M:
			right = mid - 1
		else:
			left = mid + 1
	print(left)
