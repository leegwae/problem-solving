import sys

input = sys.stdin.readline


def f(x, y, d):
	if x > w or y > h:
		return 0

	if x == w and y == h:
		return 1

	if dp[x][y][d] != -1:
		return dp[x][y][d]

	result = 0

	if d % 2 == 0:
		result += f(x + 1, y, 0)
		if d == 0:
			result += f(x, y + 1, 3)
	else:
		result += f(x, y + 1, 1)
		if d == 1:
			result += f(x + 1, y, 2)

	dp[x][y][d] = result
	return result


if __name__ == '__main__':
	w, h = map(int, input().split())
	dp = []
	for i in range(w + 1):
		dp.append([[-1] * 4 for _ in range(h + 1)])
	print((f(1, 2, 1) + f(2, 1, 0)) % 100000)

