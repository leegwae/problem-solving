import sys

input = sys.stdin.readline

MAX_INT = sys.maxsize
START = 0


def f(cur, visited):
	if visited == (1 << N) - 1:
		return W[cur][START] if W[cur][START] != 0 else MAX_INT

	if dp[cur][visited] != -1:
		return dp[cur][visited]

	result = MAX_INT
	for nxt in range(N):
		if not (visited & (1 << nxt)):
			if W[cur][nxt] != 0:
				result = min(result, f(nxt, visited | (1 << nxt)) + W[cur][nxt])

	dp[cur][visited] = result
	return result


if __name__ == '__main__':
	N = int(input())
	W = [list(map(int, input().split())) for _ in range(N)]
	dp = [[-1] * (1 << N) for _ in range(N)]
	answer = f(START, 2 ** START)
	print(answer)


