import sys
import collections

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(sy: int, sx: int) -> int:
	size = 1
	graph[sy][sx] = 0
	q = collections.deque([(sy, sx)])

	while q:
		cy, cx = q.popleft()

		for i in range(4):
			ny = cy + dy[i]
			nx = cx + dx[i]

			if 0 <= ny < N and 0 <= nx < M:
				if graph[ny][nx] == 1:
					graph[ny][nx] = 0
					size += 1
					q.append((ny, nx))

	return size


if __name__ == '__main__':
	N, M = list(map(int, input().split()))
	graph = [list(map(int, input().split())) for _ in range(N)]
	cnt, size = 0, 0
	for i in range(N):
		for j in range(M):
			if graph[i][j] == 1:
				cnt += 1
				size = max(size, bfs(i, j))

	print(cnt, size, sep='\n')