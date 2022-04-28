import sys
from collections import deque

input = sys.stdin.readline

dy = [-2, -2, -1, -1, 1, 1, 2, 2]
dx = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs(start_y, start_x):
	queue = deque([(start_y, start_x)])
	graph[start_y][start_x] = 1

	while queue:
		y, x = queue.popleft()

		for i in range(8):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= ny <= I-1 and 0 <= nx <= I-1:
				if graph[ny][nx] == 0:
					queue.append((ny, nx))
					graph[ny][nx] = graph[y][x] + 1

				if ny == ty and nx == tx:
					return


T = int(input())
for _ in range(T):
	I = int(input())
	graph = [[0] * I for _ in range(I)]
	cy, cx = list(map(int, input().split()))
	ty, tx = list(map(int, input().split()))
	bfs(cy, cx)
	print(graph[ty][tx]- 1)
