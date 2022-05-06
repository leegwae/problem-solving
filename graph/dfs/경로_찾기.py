import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


def dfs(v):
	for w in range(N):
		if graph[v][w] == 1 and visited[w] == 0:
			visited[w] = 1
			dfs(w)


for i in range(N):
	visited = [0] * N

	dfs(i)
	print(*visited, sep=" ")
