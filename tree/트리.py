import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def bfs(v):
	queue = deque([v])
	visited[v] = 1

	while queue:
		cur = queue.popleft()

		for nxt in graph[cur]:
			if visited[nxt] == 0:
				visited[nxt] = 1
				queue.append(nxt)
			elif finished[nxt] == 0:
				return False
		finished[cur] = 1

	return True


if __name__ == '__main__':
	T = 1
	while True:
		N, M = map(int, input().split())
		if N == 0 and M == 0:
			break

		graph = defaultdict(list)
		for _ in range(M):
			A, B = map(int, input().split())
			graph[A].append(B)
			graph[B].append(A)

		answer = 0
		visited = [0] * (N + 1)
		finished = [0] * (N + 1)
		for i in range(1, N + 1):
			if visited[i] == 0:
				answer += int(bfs(i))

		print(f'Case {T}:', end=' ')
		if answer == 0:
			print('No trees.')
		elif answer == 1:
			print('There is one tree.')
		else:
			print(f'A forest of {answer} trees.')

		T += 1
