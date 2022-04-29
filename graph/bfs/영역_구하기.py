import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[1] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]

for _ in range(K):
	x1, y1, x2, y2 = map(int, input().split())

	for i in range(y1, y2):
		for j in range(x1, x2):
			graph[i][j] = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(sy: int, sx: int) -> int:
	queue = deque([(sy, sx)])
	visited[sy][sx] = 1
	size = 0

	while queue:
		cy, cx = queue.popleft()
		size += 1

		for idx in range(4):
			ny = cy + dy[idx]
			nx = cx + dx[idx]

			if 0 <= ny <= M-1 and 0 <= nx <= N-1:
				if graph[ny][nx] == 1 and visited[ny][nx] == 0:
					visited[ny][nx] = 1
					queue.append((ny, nx))

	return size


count = 0
arr_size = []
for i in range(M):
	for j in range(N):
		if graph[i][j] == 1 and visited[i][j] == 0:
			arr_size.append(bfs(i, j))
			count += 1


print(count)
print(*sorted(arr_size))