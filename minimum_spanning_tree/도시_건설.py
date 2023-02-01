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
	selected = 0
	min_cost = 0
	for cost, a, b in edge:
		if find(a) == find(b):
			continue

		union(a, b)
		selected += 1
		min_cost += cost

		if selected == N - 1:
			break

	return min_cost, selected == N - 1


if __name__ == '__main__':
	N, M = map(int, input().split())
	parent = [i for i in range(N)]
	rank = [0] * N
	edge = []
	total_cost = 0
	for _ in range(M):
		a, b, c = map(int, input().split())
		edge.append((c, a-1, b-1))
		total_cost += c

	edge.sort()
	min_cost, is_connected = kruskal()

	print(total_cost - min_cost if is_connected else - 1)