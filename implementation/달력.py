import sys

input = sys.stdin.readline

if __name__ == '__main__':
	N = int(input())
	plan = []
	for _ in range(N):
		S, E = map(int, input().split())
		plan.append((S, E))
	plan.sort(key=lambda x: (x[0], -x[1]))

	graph = []
	for start, end in plan:
		line = 0
		for i, row in enumerate(graph):
			if 1 in row[start: end + 1]:
				line += 1
			else:
				break
		if len(graph) <= line:
			graph.append([0] * (365 + 1))

		for date in range(start, end + 1):
			graph[line][date] = 1

	size = 0
	width, height = 0, 0
	for i in range(1, 365 + 1):
		y = 0
		for j in range(len(graph)):
			if graph[j][i] == 1:
				y = j + 1

		if y == 0:
			size += width * height
			width, height = 0, 0
		else:
			width += 1
			height = max(height, y)
	size += width * height
	print(size)
