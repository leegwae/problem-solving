import sys
from typing import Optional, List
from collections import defaultdict, deque

input = sys.stdin.readline


def topological_sort() -> Optional[List[int]]:
	queue = deque([i for i in range(1, N + 1) if in_degree[i] == 0])
	result = []

	while queue:
		if len(queue) > 1:
			return None

		cur = queue.popleft()
		result.append(cur)
		for nxt in graph[cur]:
			in_degree[nxt] -= 1
			if in_degree[nxt] == 0:
				queue.append(nxt)

	return result if len(result) == N else None


if __name__ == '__main__':
	T = int(input())
	for _ in range(T):
		N = int(input())
		graph = defaultdict(list)
		in_degree = [0] * (N + 1)
		ranking = list(map(int, input().split()))
		for i in range(N):
			v, adj = ranking[i], ranking[i+1:]
			graph[v].extend(adj)
			for w in adj:
				in_degree[w] += 1
		M = int(input())
		for _ in range(M):
			a, b = map(int, input().split())
			u, l = (a, b) if a in graph[b] else (b, a)
			graph[l].remove(u)
			in_degree[u] -= 1
			graph[u].append(l)
			in_degree[l] += 1

		answer = topological_sort()
		if answer is None:
			print('IMPOSSIBLE')
		else:
			print(*answer)
