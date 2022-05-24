# 중복 순열
import sys

input = sys.stdin.readline


def dfs(visited):
	if len(visited) == M:
		print(*visited, sep=' ')
		return

	for i in range(1, N + 1):
		dfs([*visited, i])


if __name__ == "__main__":
	N, M = map(int, input().split())
	dfs([])
