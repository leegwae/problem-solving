import sys

input = sys.stdin.readline


def knapsack(cur, prev):
	if prev > K:
		return -1

	if cur >= N or prev == K:
		return 0

	if dp[cur][prev] != -1:
		return dp[cur][prev]

	w, v = pack[cur]
	result = knapsack(cur + 1, prev + w)
	if result != -1:
		result += v
	result = max(result, knapsack(cur + 1, prev))
	dp[cur][prev] = result

	return result


if __name__ == '__main__':
	N, K = map(int, input().split())
	pack = [tuple(map(int, input().split())) for _ in range(N)]
	dp = [[-1] * K for _ in range(N)]
	answer = knapsack(0, 0)
	print(answer)
