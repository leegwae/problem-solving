import sys
from collections import defaultdict

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def get_farthest_from(i):
	farthest, max_distance = 0, 0

	visited = [-1] * (V + 1)
	visited[i] = 0

	def dfs(v):
		nonlocal farthest, max_distance
		for w, distance in graph[v]:
			if visited[w] == -1:
				visited[w] = visited[v] + distance

				if visited[w] > max_distance:
					farthest, max_distance = w, visited[w]

				dfs(w)

	dfs(i)

	return farthest, max_distance


if __name__ == '__main__':
	V = int(input())
	graph = defaultdict(list)
	for _ in range(V):
		adj = list(map(int, input().split()))
		v = adj[0]
		for i in range(1, len(adj) - 1, 2):
			w, distance = adj[i], adj[i + 1]
			graph[v].append((w, distance))

	w, _ = get_farthest_from(1)
	_, distance = get_farthest_from(w)
	print(distance)
