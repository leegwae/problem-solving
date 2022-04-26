import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def get_count(graph):
	M, N = len(graph[0]), len(graph)

	visited = [[0] * M for _ in range(N)]

	def dfs(y, x):
		visited[y][x] = 1

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= ny <= N-1 and 0 <= nx <= M-1:
				if graph[ny][nx] == 1 and visited[ny][nx] == 0:
					dfs(ny, nx)

	count = 0

	for y in range(N):
		for x in range(M):
			if graph[y][x] == 1 and visited[y][x] == 0:
				dfs(y, x)
				count += 1

	return count


if __name__ == '__main__':
	T = int(input())

	for _ in range(T):
		M, N, K = list(map(int, input().split()))
		graph = [[0] * M for _ in range(N)]

		for _ in range(K):
			X, Y = list(map(int, input().split()))
			graph[Y][X] = 1

		print(get_count(graph))