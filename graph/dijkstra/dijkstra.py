import sys

INF = sys.maxsize


def dijkstra(start):
	visited = [0] * N
	distances = [INF] * N

	def get_closest():
		min_distance = INF
		min_pos = -1

		for i in range(N):
			if visited[i] == 0:
				if distances[i] < min_distance:
					min_pos = i
					min_distance = distances[i]

		return min_pos

	distances[start] = 0

	while True:
		closest = get_closest()

		if closest == -1:
			break

		visited[closest] = 1
		for adj in range(N):
			if graph[closest][adj] == INF or visited[adj] == 1:
				continue

			distances[adj] = min(distances[adj], distances[closest] + graph[closest][adj])

	return distances


if __name__ == '__main__':
	N = 4
	graph = [
		[INF, 2, 12, INF],
		[2, INF, INF, 4],
		[12, INF, INF, 3],
		[INF, 4, 3, INF]
	]
	START = 0
	result = dijkstra(START)
	print(result)
