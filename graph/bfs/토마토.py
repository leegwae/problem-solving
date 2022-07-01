import sys
from collections import deque

input = sys.stdin.readline

dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]


def has_unripe():
	for i in range(H):
		for j in range(N):
			for k in range(M):
				if graph[i][j][k] == 0:
					return True

	return False


def bfs():
	max_day = 1

	while queue:
		cz, cy, cx = queue.popleft()

		for i in range(6):
			nz = cz + dz[i]
			ny = cy + dy[i]
			nx = cx + dx[i]

			if 0 <= nz <= H - 1 and 0 <= ny <= N - 1 and 0 <= nx <= M - 1:
				if graph[nz][ny][nx] == 0:
					graph[nz][ny][nx] = graph[cz][cy][cx] + 1
					queue.append((nz, ny, nx))
					max_day = max(max_day, graph[nz][ny][nx])

	return max_day - 1


if __name__ == '__main__':
	# 가로, 세로, 높이
	M, N, H = map(int, input().split())
	queue = deque([])
	graph = []
	# 1: 익은 토마토
	# 0: 익지 않은 토마토
	# -1: 토마토가 들어있지 않음
	for i in range(H):
		board = []
		for j in range(N):
			line = list(map(int, input().split()))

			for k in range(M):
				if line[k] == 1:
					queue.append((i, j, k))

			board.append(line)

		graph.append(board)

	result = bfs()
	print(-1 if has_unripe() else result)
