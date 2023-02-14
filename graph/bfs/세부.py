import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def bfs(limit):
	visited = [0] * (N + 1)
	queue = deque([s])
	visited[s] = 1

	while queue:
		cur = queue.popleft()

		for nxt, weight in graph[cur]:
			if visited[nxt] == 0 and limit <= weight:
				if nxt == e:
					return True

				queue.append(nxt)
				visited[nxt] = 1

	return False


def dfs(limit):
	visited = [0] * (N + 1)
	stack = [s]
	visited[s] = 1

	while stack:
		cur = stack.pop()

		for nxt, weight in graph[cur]:
			if visited[nxt] == 0 and limit <= weight:
				if nxt == e:
					return True

				stack.append(nxt)
				visited[nxt] = 1

	return False


if __name__ == '__main__':
	N, M = map(int, input().split())
	s, e = map(int, input().split())
	graph = defaultdict(list)
	high = 1
	for _ in range(M):
		h1, h2, k = map(int, input().split())
		graph[h1].append((h2, k))
		graph[h2].append((h1, k))
		high = max(high, k)

	low = 0
	while low < high:
		mid = (low + high) // 2
		if dfs(mid):
			low = mid + 1
		else:
			high = mid - 1

	print(low)