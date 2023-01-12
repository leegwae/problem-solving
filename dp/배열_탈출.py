import sys

INF = int(1e09)
input = sys.stdin.readline


if __name__ == '__main__':
	N = int(input())
	A = [list(map(int, input().split())) for _ in range(N)]
	dp = [[0] * N for _ in range(N)]

	for y in range(N):
		for x in range(N):
			if y == 0 and x == 0:
				continue

			up, left = INF, INF
			if y >= 1:
				up = dp[y - 1][x]
				if A[y][x] >= A[y - 1][x]:
					up += A[y][x] - A[y - 1][x] + 1

			if x >= 1:
				left = dp[y][x - 1]
				if A[y][x] >= A[y][x - 1]:
					left += A[y][x] - A[y][x - 1] + 1

			dp[y][x] = min(up, left)

	print(dp[N - 1][N - 1])
