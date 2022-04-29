import sys
import collections

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = collections.defaultdict(list)

for _ in range(1, M+1):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)

visited = [0] * (N+1)


def dfs(v):
	visited[v] = 1

	for w in graph[v]:
		if visited[w] == 0:
			dfs(w)


count = 0
for i in range(1, N+1):
	if visited[i] == 0:
		dfs(i)
		count += 1

print(count)