import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(cy: int, cx: int) -> None:
	visited[cy][cx] = 1

	for i in range(4):
		ny = cy + dy[i]
		nx = cx + dx[i]

		if 0 <= ny <= N-1 and 0 <= nx <= M-1:
			if matrix[ny][nx] == 1 and visited[ny][nx] == 0:
				dfs(ny, nx)


T = int(input())
for _ in range(T):
	M, N, K = list(map(int, input().split()))
	matrix, visited = [], []

	for _ in range(N):
		matrix.append([0] * M)
		visited.append([0] * M)

	for _ in range(K):
		X, Y = list(map(int, input().split()))
		matrix[Y][X] = 1

	count = 0

	for y in range(N):
		for x in range(M):
			if matrix[y][x] == 1 and visited[y][x] == 0:
				dfs(y, x)
				count += 1
	print(count)