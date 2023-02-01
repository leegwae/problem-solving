import sys

input = sys.stdin.readline


def find(u):
	if u == parent[u]:
		return u
	parent[u] = find(parent[u])
	return parent[u]


def union(u, v):
	u, v = find(u), find(v)

	if u == v:
		return

	if rank[u] > rank[v]:
		u, v = v, u

	parent[u] = v

	if rank[u] == rank[v]:
		rank[v] += 1


def kruskal():
	edges = []
	edges.sort()

	selected = []
	total = 0
	for cost, a, b in edges:
		if find(a) == find(b):
			continue

		union(a, b)
		selected.append((a, b))
		total += cost
	return selected, total


if __name__ == '__main__':
	N = int(input())
	graph = [[] for _ in range(N)]

	parent = [i for i in range(N)]
	rank = [0] * N

