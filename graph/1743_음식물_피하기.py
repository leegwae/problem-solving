import sys
import collections

sys.setrecursionlimit(10000)

n, m, k = map(int, input().split())
arr = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(k):
	r, c = map(int, input().split())
	arr[r][c] = 1


visited = [[0] * (m + 1) for _ in range(n + 1)]


# def dfs(cy, cx):
# 	if cy < 1 or cy > n or\
# 		cx < 1 or cx > m or\
# 		arr[cy][cx] != 1 or\
# 		visited[cy][cx] != 0:
# 		return 0
#
# 	visited[cy][cx] = 1
# 	size = 1
# 	size += dfs(cy - 1, cx)
# 	size += dfs(cy + 1, cx)
# 	size += dfs(cy, cx - 1)
# 	size += dfs(cy, cx + 1)
#
# 	return size

# def dfs(cy, cx):
# 	if cy < 1 or cy > n or\
# 		cx < 1 or cx > m or\
# 		arr[cy][cx] != 1:
# 		return 0
#
# 	arr[cy][cx] = 0
# 	size = 1
# 	size += dfs(cy - 1, cx)
# 	size += dfs(cy + 1, cx)
# 	size += dfs(cy, cx - 1)
# 	size += dfs(cy, cx + 1)
#
# 	return size


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(cy, cx):
	visited[cy][cx] = 1
	size = 1

	for i in range(4):
		ny = cy + dy[i]
		nx = cx + dx[i]
		if 1 <= ny <= n and 1 <= nx <= m:
			if arr[ny][nx] == 1 and visited[ny][nx] == 0:
				size += dfs(ny, nx)
	return size


def bfs(cy, cx):
	visited[cy][cx] = 1
	size = 1
	queue = collections.deque()
	queue.append((cy, cx))

	while queue:
		x, y = queue.popleft()

		for i in range(4):
			ny = x + dy[i]
			nx = y + dx[i]

			if 1 <= ny <= n and 1 <= nx <= m:
				if arr[ny][nx] == 1 and visited[ny][nx] == 0:
					visited[ny][nx] = 1
					queue.append((ny, nx))
					size += 1

	return size


mx = 0
for i in range(1, n + 1):
	for j in range(1, m + 1):
		if arr[i][j] == 1 and visited[i][j] == 0:
			mx = max(mx, bfs(i, j))
			# mx = max(mx, dfs(i, j))

print(mx)