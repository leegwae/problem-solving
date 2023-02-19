import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
	max_v, max_dist = -1, -1
	dist = [-1] * (N+1)
	queue = deque([start])
	dist[start] = 0

	while queue:
		cur = queue.popleft()

		for nxt in graph[cur]:
			if dist[nxt] == -1:
				dist[nxt] = dist[cur] + 1
				queue.append(nxt)

				if dist[nxt] > max_dist:
					max_v, max_dist = nxt, dist[nxt]

	return max_v, max_dist


if __name__ == '__main__':
	N = int(input())
	graph = [[] for _ in range(N+1)]
	for _ in range(N-1):
		u, v = map(int, input().split())
		graph[u].append(v)
		graph[v].append(u)

	w, _ = bfs(1)
	_, dist = bfs(w)
	print(dist // 2 + dist % 2)
