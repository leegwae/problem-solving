import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def topological_sort():
	queue = deque([i for i in range(1, N + 1) if in_degree[i] == 0])

	for _ in range(N):
		if not queue:
			return False

		cur = queue.popleft()
		path.append(cur)
		for nxt in graph[cur]:
			in_degree[nxt] -= 1
			if in_degree[nxt] == 0:
				queue.append(nxt)

	return True


if __name__ == '__main__':
	N, M = map(int, input().split())
	graph = defaultdict(list)
	in_degree = [0] * (N + 1)
	for _ in range(M):
		n, *order = list(map(int, input().split()))
		for i in range(n - 1):
			in_degree[order[i + 1]] += 1
			graph[order[i]].append(order[i + 1])

	path = []
	if topological_sort():
		print(*path, sep='\n')
	else:
		print(0)
