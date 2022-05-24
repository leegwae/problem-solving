import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
MAX_SIZE = 100000 + 1


def f(cur, acc):
	if acc == k:
		return 0

	if cur >= n or acc > k:
		return MAX_SIZE

	if dp[cur][acc] != -1:
		return dp[cur][acc]

	result = min(f(cur, acc + coins[cur]) + 1, f(cur + 1, acc))
	dp[cur][acc] = result

	return result


if __name__ == '__main__':
	n, k = map(int, input().split())
	coins = [int(input()) for _ in range(n)]
	dp = [[-1] * k for _ in range(n)]
	answer = f(0, 0)
	print(-1 if answer == MAX_SIZE else answer)