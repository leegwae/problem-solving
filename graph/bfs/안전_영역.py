import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(sy, sx, height):
	queue = deque([(sy, sx)])
	visited[sy][sx] = 1

	while queue:
		cy, cx = queue.popleft()

		for idx in range(4):
			ny = cy + dy[idx]
			nx = cx + dx[idx]

			if 1 <= ny <= N and 1 <= nx <= N:
				if graph[ny][nx] > height and visited[ny][nx] == 0:
					visited[ny][nx] = 1
					queue.append((ny, nx))


def get_count_of_component(height):
	count = 0

	for i in range(1, N + 1):
		for j in range(1, N + 1):
			if graph[i][j] > height and visited[i][j] == 0:
				bfs(i, j, height)
				count += 1

	return count


N = int(input())
graph = [[0] * (N + 1)]

for _ in range(N):
	graph.append([0, *list(map(int, input().split()))])

max_count = 0
max_height = max(map(max, graph))

for h in range(max_height):
	visited = [[0] * (N + 1) for _ in range(N + 1)]
	max_count = max(max_count, get_count_of_component(h))

print(max_count)