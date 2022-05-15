import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def f(x, y):
	if x == n:
		return 0
	if dp[x][y] != - 1:
		return dp[x][y]

	result = f(x + 1, -1)
	# [0][x-1]의 스티커를 떼지 않았다면
	if y != 0:
		# [0][x]의 스티커를 뗀다.
		result = max(result, f(x + 1, 0) + s[0][x])
	# [1][x-1]의 스티커를 떼지 않았다면
	if y != 1:
		# [1][x]의 스티커를 뗀다.
		result = max(result, f(x + 1, 1) + s[1][x])

	dp[x][y] = result

	return result


if __name__ == "__main__":
	T = int(input())
	for _ in range(T):
		n = int(input())
		s = [list(map(int, input().split())) for _ in range(2)]
		dp = [dict.fromkeys(list(range(-1, 2)), -1) for _ in range(n)]
		answer = f(0, -1)
		print(answer)
