import sys
from collections import defaultdict, deque

INF = 1e09
input = sys.stdin.readline


def bfs(start: int):
	queue = deque([start])
	distance = [-INF] * (N + 1)
	distance[start] = 0

	while queue:
		cur = queue.popleft()

		for nxt in graph[cur]:
			if distance[nxt] == -INF:
				distance[nxt] = distance[cur] + 1
				queue.append(nxt)
	return distance


if __name__ == '__main__':
	N, M = map(int, input().split())
	graph = defaultdict(list)
	for _ in range(M):
		A, B = map(int, input().split())
		graph[A].append(B)
		graph[B].append(A)

	d = bfs(1)
	max_distance = max(d)
	print(d.index(max_distance), max_distance, d.count(max_distance))
