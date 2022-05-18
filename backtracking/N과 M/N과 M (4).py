import sys

input = sys.stdin.readline


def dfs(cur, visited):
	if len(visited) == M:
		print(*visited, sep=' ')
		return

	for nxt in range(cur, N + 1):
		dfs(nxt, [*visited, nxt])


if __name__ == '__main__':
	N, M = map(int, input().split())
	dfs(1, [])
