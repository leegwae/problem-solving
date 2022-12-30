from typing import List, Tuple
import sys
from heapq import heappop, heappush


input = sys.stdin.readline
INF = 1e9


def dijkstra(start: int) -> List[int]:
	distance = [INF] * (V + 1)
	distance[start] = 0
	queue = [(0, start)]

	while queue:
		cur_dist, cur = heappop(queue)

		if cur_dist > distance[cur]:
			continue

		for nxt, weight in graph[cur]:
			nxt_dist = cur_dist + weight

			if nxt_dist < distance[nxt]:
				distance[nxt] = nxt_dist
				heappush(queue, (nxt_dist, nxt))

	return distance


if __name__ == '__main__':
	V, E, P = map(int, input().split())
	graph: List[List[Tuple[int, int]]] = [[] for _ in range(V + 1)]
	for _ in range(E):
		a, b, c = map(int, input().split())
		graph[a].append((b, c))
		graph[b].append((a, c))

	distance_m = dijkstra(1)
	distance_g = dijkstra(P)
	print('SAVE HIM' if distance_m[V] == distance_m[P] + distance_g[V] else 'GOOD BYE')
