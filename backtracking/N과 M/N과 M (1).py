import sys

input = sys.stdin.readline


def dfs(visited):
	if len(visited) == M:
		print(*visited, sep=" ")
		return

	for nxt in range(1, N + 1):
		if nxt not in visited:
			dfs([*visited, nxt])


if __name__ == '__main__':
	N, M = map(int, input().split())
	dfs([])
