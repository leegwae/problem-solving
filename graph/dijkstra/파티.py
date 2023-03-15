import sys
from typing import List, Tuple
from heapq import heappush, heappop

input = sys.stdin.readline


INF = int(1e09)


def bfs(start, graph):
	dist = [INF] * (N + 1)
	queue = [(0, start)]
	dist[start] = 0

	while queue:
		cur_dist, cur = heappop(queue)

		if cur_dist > dist[cur]:
			continue

		for nxt, cost in graph[cur]:
			nxt_dist = cur_dist + cost

			if dist[nxt] > nxt_dist:
				dist[nxt] = nxt_dist
				heappush(queue, (nxt_dist, nxt))

	return dist


if __name__ == '__main__':
	N, M, X = map(int, input().split())
	g1: List[List[Tuple[int, int]]] = [[] for _ in range(N + 1)]
	g2: List[List[Tuple[int, int]]] = [[] for _ in range(N + 1)]
	for _ in range(M):
		A, B, T = map(int, input().split())
		g1[A].append((B, T))
		g2[B].append((A, T))
	d1, d2 = bfs(X, g1), bfs(X, g2)
	print(max(d1[i] + d2[i] for i in range(1, N + 1)))
