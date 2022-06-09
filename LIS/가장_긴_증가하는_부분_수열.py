import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


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


if __name__ == '__main__':
	N = int(input())
	A = list(map(int, input().split()))
	dp = [[-1] * N for _ in range(N)]
	answer = f(-1, 0)
	print(answer)
