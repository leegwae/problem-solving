import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())
a, b = list(map(int, input().split()))
m = int(input())

graph = defaultdict(list)
visited = [0] * (n + 1)

for _ in range(m):
	x, y = list(map(int, input().split()))
	graph[x].append(y)
	graph[y].append(x)

level = [0] * (n + 1)


def bfs(v: int) -> None:
	queue = deque([v])
	visited[v] = 1

	while queue:
		cur = queue.popleft()

		for w in graph[cur]:
			if visited[w] == 0:
				level[w] = level[cur] + 1
				queue.append(w)
				visited[w] = 1


bfs(a)
print(level[b] if level[b] != 0 else -1)
