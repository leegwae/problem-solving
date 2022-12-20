import sys
from typing import Tuple, List
from heapq import heappop, heappush

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start: int) -> List[int]:
	distances = [INF] * (N + 1)
	distances[start] = 0

	queue = []
	heappush(queue, (distances[start], start))

	while queue:
		cur_dist, cur = heappop(queue)

		if distances[cur] < cur_dist:
			continue

		for nxt, weight in graph[cur]:
			nxt_dist = cur_dist + weight

			if nxt_dist < distances[nxt]:
				distances[nxt] = nxt_dist
				heappush(queue, (nxt_dist, nxt))

	return distances


if __name__ == '__main__':
	N = int(input())
	A, B, C = list(map(int, input().split()))
	M = int(input())
	graph: List[List[Tuple[int, int]]] = [[] for _ in range(N + 1)]
	for _ in range(M):
		D, E, L = list(map(int, input().split()))

		graph[D].append((E, L))
		graph[E].append((D, L))

	d_A = dijkstra(A)
	d_B = dijkstra(B)
	d_C = dijkstra(C)

	max_d = 0
	answer = 0
	for i in range(1, N + 1):
		cur_d = min(d_A[i], d_B[i], d_C[i])
		if cur_d > max_d:
			max_d = cur_d
			answer = i

	print(answer)

