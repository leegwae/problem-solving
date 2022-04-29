import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
graph = [[0] * (N + 1)]

for _ in range(N):
	graph.append([0, *list(map(int, input().split()))])

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(cy, cx, height):
	visited[cy][cx] = 1

	for idx in range(4):
		ny = cy + dy[idx]
		nx = cx + dx[idx]

		if 1 <= ny <= N and 1 <= nx <= N:
			if graph[ny][nx] > height and visited[ny][nx] == 0:
				dfs(ny, nx, height)


def get_component_count(height):
	count = 0

	for i in range(1, N+1):
		for j in range(1, N+1):
			if graph[i][j] > height and visited[i][j] == 0:
				dfs(i, j, height)
				count += 1

	return count


max_height = max(map(max, graph))
max_count = 0

for h in range(max_height):
	visited = [[0] * (N + 1) for _ in range(N + 1)]
	count = get_component_count(h)
	max_count = max(max_count, count)

print(max_count)
