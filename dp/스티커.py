import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def f(col, prev):
	if col == n:
		return 0
	if dp[col][prev] != - 1:
		return dp[col][prev]

	result = f(col + 1, -1)
	if prev != 0:
		result = max(result, f(col + 1, 0) + s[0][col])
	if prev != 1:
		result = max(result, f(col + 1, 1) + s[1][col])
	dp[col][prev] = result

	return result


if __name__ == "__main__":
	T = int(input())
	for _ in range(T):
		n = int(input())
		s = [list(map(int, input().split())) for _ in range(2)]
		dp = [dict.fromkeys(list(range(-1, 2)), -1) for _ in range(n)]
		answer = f(0, -1)
		print(answer)
