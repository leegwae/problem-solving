import sys

input = sys.stdin.readline


def f(t: int, w: int) -> int:
	if t > T or w > W:
		return 0

	if dp[t][w] != -1:
		return dp[t][w]

	cur = 1 if w % 2 == 0 else 2

	result = 1 if tree[t] == cur else 0
	result += max(f(t + 1, w), f(t + 1, w + 1))
	dp[t][w] = result

	return result


if __name__ == "__main__":
	T, W = map(int, input().split())
	tree = [0, *[int(input()) for _ in range(T)]]
	dp = [[-1] * (W + 1) for _ in range(T + 1)]
	print(max(f(0, 0), f(0, 1)))
