import sys
from typing import List
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y: int, x: int) -> (int, List[int]):
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


if __name__ == '__main__':
	N = int(input())
	pos = (-1, -1)
	size = 2
	fish = 0
	graph = []
	for i in range(N):
		l = list(map(int, input().split()))
		for j in range(N):
			if l[j] != 0:
				if l[j] == 9:
					pos = (i, j)
					l[j] = 0
				else:
					fish += 1
		graph.append(l)

	ate = 0
	answer = 0
	while fish:
		m_distance, m_position = bfs(*pos)

		if not m_position:
			break

		m_position.sort()
		pos = m_position[0]
		answer += m_distance

		ny, nx = pos
		ate += 1
		fish -= 1
		graph[ny][nx] = 0

		if ate == size:
			size += 1
			ate = 0
	print(answer)
