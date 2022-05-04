import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, list(input().strip())))for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(cy, cx):
	count = 1
	visited[cy][cx] = 1

	for i in range(4):
		ny = cy + dy[i]
		nx = cx + dx[i]

		if 0 <= ny <= N - 1 and 0 <= nx <= N - 1:
			if graph[ny][nx] == 1 and visited[ny][nx] == 0:
				visited[ny][nx] = 1
				count += dfs(ny, nx)

	return count


component_count = 0
components = []
for i in range(N):
	for j in range(N):
		if graph[i][j] == 1 and visited[i][j] == 0:
			components.append(dfs(i, j))
			component_count += 1


print(component_count)
print(*sorted(components), sep="\n")