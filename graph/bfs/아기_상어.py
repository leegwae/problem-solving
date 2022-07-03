import sys
from typing import List, Tuple
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y: int, x: int, size: int) -> (int, List[Tuple[int, int]]):
	distance = [[-1] * N for _ in range(N)]
	queue = deque([(y, x)])
	distance[y][x] = 0

	min_distance, min_position = INF, []

	while queue:
		cy, cx = queue.popleft()

		for i in range(4):
			ny = cy + dy[i]
			nx = cx + dx[i]

			if 0 <= ny < N and 0 <= nx < N:
				if distance[ny][nx] == -1:
					if graph[ny][nx] <= size:
						distance[ny][nx] = distance[cy][cx] + 1
						queue.append((ny, nx))

						if 0 < graph[ny][nx] < size:
							if distance[ny][nx] < min_distance:
								min_distance = distance[ny][nx]
								min_position = [(ny, nx)]
							elif distance[ny][nx] == min_distance:
								min_position.append((ny, nx))

	return min_distance, min_position


def get_time() -> int:
	global shark_pos, fish_cnt

	shark_size = 2
	shark_ate = 0
	time = 0

	while fish_cnt:
		m_distance, m_position = bfs(*shark_pos, shark_size)

		if not m_position:
			break

		m_position.sort()

		time += m_distance
		shark_pos = m_position[0]
		shark_ate += 1
		fish_cnt -= 1
		graph[shark_pos[0]][shark_pos[1]] = 0

		if shark_ate == shark_size:
			shark_size += 1
			shark_ate = 0

	return time


if __name__ == '__main__':
	N = int(input())
	shark_pos = (-1, -1)
	fish_cnt = 0

	graph = []
	for i in range(N):
		l = list(map(int, input().split()))
		for j in range(N):
			if l[j] != 0:
				if l[j] == 9:
					shark_pos = (i, j)
					l[j] = 0
				else:
					fish_cnt += 1
		graph.append(l)

	answer = get_time()
	print(answer)
