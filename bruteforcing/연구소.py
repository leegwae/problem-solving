import sys
import copy

input = sys.stdin.readline

sys.setrecursionlimit(100000)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
zero_list = [(i, j) for j in range(M) for i in range(N) if graph[i][j] == 0]
zero_len = len(zero_list)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(cy, cx):
	for i in range(4):
		ny = cy + dy[i]
		nx = cx + dx[i]

		if 0 <= ny <= N - 1 and 0 <= nx <= M - 1:
			if copied[ny][nx] == 0:
				copied[ny][nx] = 2
				dfs(ny, nx)


def get_safe_count(matrix):
	count = 0

	for i in range(N):
		for j in range(M):
			if matrix[i][j] == 0:
				count += 1
	return count


max_count = 0
for i in range(zero_len - 2):
	for j in range(i + 1, zero_len - 1):
		for k in range(j + 1, zero_len):
			copied = copy.deepcopy(graph)
			for idx in [i, j, k]:
				y, x = zero_list[idx]
				copied[y][x] = 1

			for n in range(N):
				for m in range(M):
					if graph[n][m] == 2:
						dfs(n, m)
			max_count = max(max_count, get_safe_count(copied))
print(max_count)
