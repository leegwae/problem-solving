import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def bottom_up():
	dp = [1] * N

	def f(n):
		for cur in range(1, n):
			for prev in range(0, cur):
				if A[cur] > A[prev]:
					dp[cur] = max(dp[cur], dp[prev] + 1)

		return max(dp)

	return f(N)


def top_down():
	AA = [0] + A
	NN = len(AA)
	dp = [-1] * NN

	def f(cur):
		if dp[cur] != -1:
			return dp[cur]

		result = 0
		for nxt in range(cur + 1, NN):
			if AA[nxt] > AA[cur]:
				result = max(result, f(nxt) + 1)
		dp[cur] = result

		return result

	return f(0)


# def LIS_3():
# 	dp = [[-1] * N for _ in range(N)]
#
# 	def f(prev, cur):
# 		if cur == N:
# 			return 0
#
# 		if dp[prev][cur] != -1:
# 			return dp[prev][cur]
#
# 		result = f(prev, cur + 1)
# 		if prev == -1 or A[prev] < A[cur]:
# 			result = max(result, f(cur, cur + 1) + 1)
# 		dp[prev][cur] = result
#
# 		return result
#
# 	print(f(-1, 0))


def brute_forcing():
	def f(arr):
		if len(arr) == 0:
			return 0

		result = 1
		for cur in range(0, len(arr)):
			s = []
			for nxt in range(cur + 1, len(arr)):
				if arr[cur] < arr[nxt]:
					s.append(arr[nxt])
			result = max(result, f(s) + 1)
		return result

	return f(A)


if __name__ == '__main__':
	N = int(input())
	A = list(map(int, input().split()))
	# answer = brute_forcing()
	answer = bottom_up()
	# answer = top_down()
	print(answer)
