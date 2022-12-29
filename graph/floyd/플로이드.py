import sys
import math

INF = math.inf
input = sys.stdin.readline

if __name__ == '__main__':
	N = int(input())
	M = int(input())
	graph = [[INF] * (N + 1) for _ in range(N + 1)]

	for _ in range(M):
		a, b, c = list(map(int, input().split()))
		graph[a][b] = min(graph[a][b], c)

	for k in range(1, N + 1):
		graph[k][k] = 0
		for i in range(1, N + 1):
			for j in range(1, N + 1):
				graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

	for row in graph[1:]:
		for cost in row[1:]:
			print(0 if cost == INF else cost, end=' ')
		print()
