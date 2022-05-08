import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def bfs_swan(queue: deque):
	global found
	temp = deque()

	while queue:
		cy, cx = queue.popleft()
		if (cy, cx) == swan[1]:
			found = True
			return

		for i in range(4):
			ny = cy + dy[i]
			nx = cx + dx[i]

			if 0 <= ny <= R - 1 and 0 <= nx <= C - 1:
				if graph[ny][nx] != '-':
					if graph[ny][nx] != 'X':
						queue.append((ny, nx))
					else:
						temp.append((ny, nx))
					graph[ny][nx] = '-'
	return temp


def bfs_water(queue):
	temp = deque()

	while queue:
		cy, cx = queue.popleft()
		for i in range(4):
			ny = cy + dy[i]
			nx = cx + dx[i]
			if 0 <= ny <= R - 1 and 0 <= nx <= C - 1:
				if graph[ny][nx] == 'X':
					graph[ny][nx] = '.'
					temp.append((ny, nx))

	return temp


if __name__ == '__main__':
	R, C = map(int, input().split())
	graph, swan = [], []
	water_q, swan_q = deque(), deque()

	for i in range(R):
		row = list(input().rstrip())
		for j, ch in enumerate(row):
			if ch != 'X':
				water_q.append((i, j))

				if ch == 'L':
					swan.append((i, j))
		graph.append(row)

	y, x = swan[0]
	swan_q.append((y, x))
	graph[y][x] = '-'

	found = False
	day = 0
	while True:
		swan_q = bfs_swan(swan_q)
		if found:
			break
		water_q = bfs_water(water_q)
		day += 1

	print(day)