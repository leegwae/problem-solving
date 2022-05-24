# 조합
import sys

input = sys.stdin.readline


def dfs(cur, visited):
	if len(visited) == M:
		print(*visited, sep=" ")
		return

	if cur > N:
		return

	dfs(cur + 1, [*visited, cur])
	dfs(cur + 1, [*visited])


if __name__ == '__main__':
	N, M = map(int, input().split())
	dfs(1, [])
