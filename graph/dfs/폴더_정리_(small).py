import sys
from collections import defaultdict
input = sys.stdin.readline

if __name__ == '__main__':
	N, M = map(int, input().split())
	graph = {}
	for _ in range(N + M):
		# 상위 이름, 하위 이름, 폴더인가
		P, F, C = list(input().split())
		C = int(C)

		if P not in graph:
			graph[P] = {
				'folders': [],
				'files': []
			}

		if C:
			graph[P]['folders'].append(F)
			if F not in graph:
				graph[F] = {
				'folders': [],
				'files': []
			}
		else:
			graph[P]['files'].append(F)

	Q = int(input())
	for _ in range(Q):
		query = input().rstrip().split('/')

		stack = [query[-1]]
		visited = defaultdict(bool)
		visited[query[-1]] = True

		files, cnt = [], 0
		while stack:
			cur = stack.pop()

			files += graph[cur]['files']
			cnt += len(graph[cur]['files'])

			for nxt in graph[cur]['folders']:
				stack.append(nxt)
		print(len(set(files)), cnt)
