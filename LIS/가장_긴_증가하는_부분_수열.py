import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def LIS_1():
	dp = [1] * N

	def f(n):
		for cur in range(1, n):
			for prev in range(0, cur):
				if A[cur] > A[prev]:
					dp[cur] = max(dp[cur], dp[prev] + 1)

		return max(dp)

	print(f(N))


def LIS_2():
	AA = [0] + A
	dp = [-1] * (N + 1)

	def f(cur):
		if dp[cur] != -1:
			return dp[cur]

		result = 0
		for nxt in range(cur + 1, N + 1):
			if AA[nxt] > AA[cur]:
				result = max(result, f(nxt) + 1)
		dp[cur] = result

		return result

	print(f(0))


def LIS_3():
	dp = [[-1] * N for _ in range(N)]

	def f(prev, cur):
		if cur == N:
			return 0

		if dp[prev][cur] != -1:
			return dp[prev][cur]

		result = f(prev, cur + 1)
		if prev == -1 or A[prev] < A[cur]:
			result = max(result, f(cur, cur + 1) + 1)
		dp[prev][cur] = result

		return result

	print(f(-1, 0))


if __name__ == '__main__':
	N = int(input())
	A = list(map(int, input().split()))
	LIS_1()
	# LIS_2()
	# LIS_3()
