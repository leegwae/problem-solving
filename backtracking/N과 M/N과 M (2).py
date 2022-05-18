import sys

input = sys.stdin.readline


def dfs(cur, prev):
	if len(prev) == M:
		print(*prev, sep=" ")
		return

	if cur > N:
		return

	dfs(cur + 1, [*prev, cur])
	dfs(cur + 1, [*prev])


if __name__ == '__main__':
	N, M = map(int, input().split())
	dfs(1, [])
