import sys
from collections import deque

input = sys.stdin.readline

N, M = list(map(int, input().split()))
maze = [[0] * (M + 1)]

for _ in range(1, N+1):
	maze.append([0, *list(map(int, input().strip()))])

dy = [-1, 1, 0, 0]
dx = [0,0, -1, 1]


def bfs(y, x):
	queue = deque()
	queue.append((y, x))

	while queue:
		cy, cx = queue.popleft()

		for i in range(4):
			ny = cy + dy[i]
			nx = cx + dx[i]

			if 1 <= ny <= N and 1 <= nx <= M:
				if maze[ny][nx] == 1:
					maze[ny][nx] = maze[cy][cx] + 1
					queue.append((ny, nx))
					if ny == N and nx == M:
						return


bfs(1,1)
print(maze[N][M])