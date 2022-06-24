import sys
from typing import Tuple, List
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start: int) -> List[int]:
	distances = [INF] * (V + 1)

	distances[start] = 0
	queue: List[Tuple[int, int]] = [(distances[start], start)]

	while queue:
		cur_dist, cur = heappop(queue)

		if distances[cur] < cur_dist:
			continue

		for nxt, weight in graph[cur].items():
			nxt_dist = cur_dist + weight

			if nxt_dist < distances[nxt]:
				distances[nxt] = nxt_dist
				heappush(queue, (nxt_dist, nxt))

	return distances


if __name__ == '__main__':
	V, E = map(int, input().split())
	K = int(input())
	graph = defaultdict(dict)
	for _ in range(E):
		u, v, w = map(int, input().split())
		graph[u][v] = w

	result = dijkstra(K)
	for v in range(1, V + 1):
		if result[v] == INF:
			print('INF')
		else:
			print(result[v])
