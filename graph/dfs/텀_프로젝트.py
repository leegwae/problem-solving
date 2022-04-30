import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(v):
	global count
	visited[v] = 1
	cycle.append(v)

	w = graph[v]
	if visited[w] == 0:
		dfs(w)
	else:
		if w in cycle:
			count += len(cycle[cycle.index(w):])
			return


T = int(input())
for _ in range(T):
	n = int(input())
	graph = [0, *list(map(int, input().split()))]
	visited = [0] * (n + 1)
	count = 0

	for i in range(1, n + 1):
		if visited[i] == 0:
			cycle = []
			dfs(i)

	print(n - count)


