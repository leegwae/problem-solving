from typing import Optional, List
from collections import deque


# using queue
def topological_sort() -> Optional[List[int]]:
	in_degree = [0, 0, 1, 2, 2, 1, 0]
	queue = deque([i for i in range(1, N + 1) if in_degree[i] == 0])
	path = []

	while queue:
		cur = queue.popleft()
		path.append(cur)
		for nxt in graph[cur]:
			in_degree[nxt] -= 1
			if in_degree[nxt] == 0:
				queue.append(nxt)

	return path if len(path) == N else None


# using stack
def dfs_all() -> Optional[List[int]]:
	visited = [0] * (N + 1)
	has_cycle = False
	path = []

	def dfs(cur):
		nonlocal has_cycle

		visited[cur] = 1
		for nxt in graph[cur]:
			if visited[nxt] == 0:
				dfs(nxt)
			elif nxt not in path:
				has_cycle = True
				return

		path.append(cur)

	for i in range(1, N + 1):
		if has_cycle:
			break

		if visited[i] == 0:
			dfs(i)

	return path[::-1] if not has_cycle else None


if __name__ == '__main__':
	N = 6
	graph = {
		1: [4],
		2: [3, 5],
		3: [],
		4: [3],
		5: [4],
		6: [2]
	}
	sorted_path = topological_sort()
	# sorted_path = dfs_all()
	print(sorted_path)
