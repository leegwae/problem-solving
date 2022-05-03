import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
box = []
queue = deque()
for i in range(N):
	tomato = list(map(int, input().split()))
	box.append(tomato)
	queue.extend([(i, j) for j, t in enumerate(tomato) if t == 1])


def has_zero(matrix):
	for i in range(0, N):
		for j in range(0, M):
			if matrix[i][j] == 0:
				return True
	return False


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(queue):
	max_day = 1
	while queue:
		cy, cx = queue.popleft()
		max_day = max(max_day, box[cy][cx])

		for i in range(4):
			ny = cy + dy[i]
			nx = cx + dx[i]

			if 0 <= ny <= N - 1 and 0 <= nx <= M - 1:
				if box[ny][nx] == 0:
					box[ny][nx] = box[cy][cx] + 1
					queue.append((ny, nx))

	return max_day


max_day = bfs(queue)
print(-1 if has_zero(box) else max_day - 1)