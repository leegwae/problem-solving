import sys
from typing import List, Tuple

INF = int(1e09)
input = sys.stdin.readline


def bellman_ford(start) -> List[int]:
	dist = [INF] * (N + 1)
	dist[start] = 0

	for i in range(N):
		for cur, nxt, weight in graph:
			if dist[cur] != INF and dist[nxt] > dist[cur] + weight:
				dist[nxt] = dist[cur] + weight
				if i == N - 1:
					return []
	return dist


if __name__ == '__main__':
	N, M = map(int, input().split())
	graph: List[Tuple[int, int, int]] = []
	for _ in range(M):
		A, B, C = map(int, input().split())
		graph.append((A, B, C))

	dist = bellman_ford(1)

	if not dist:
		print(-1)
	else:
		for i in range(2, N + 1):
			print(-1 if dist[i] == INF else dist[i])
