import sys

input = sys.stdin.readline
INF = int(1e09)


def bellman_ford(start):
	dist = [INF] * N
	dist[start] = 0

	for i in range(N):
		updated = False
		for cur, nxt, cost in edges:
			if dist[cur] != INF and dist[nxt] > dist[cur] + cost:
				dist[nxt] = dist[cur] + cost
				updated = True

				if i == N - 1:
					return []
		if not updated:
			break

	return dist


if __name__ == '__main__':
	N, M = map(int, input().split())
	edges = [tuple(map(int, input().split())) for _ in range(M)]
	print(bellman_ford(1))
