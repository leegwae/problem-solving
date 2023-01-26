import sys

input = sys.stdin.readline


def f(x: int):
	if visited[x] == 1:
		return

	result = [0] * (N + 1)
	if sum(part[x]) == 0:
		result[x] = 1
	else:
		for y, k in enumerate(part[x]):
			if x == y or k == 0:
				continue
			f(y)
			for i in range(1, N + 1):
				result[i] += part[y][i] * k

	visited[x] = 1
	part[x] = result


if __name__ == '__main__':
	N = int(input())
	M = int(input())
	part = [[0] * (N + 1) for _ in range(N + 1)]
	for _ in range(M):
		x, y, k = map(int, input().split())
		part[x][y] = k

	visited = [0] * (N + 1)
	f(N)
	for y in range(1, N + 1):
		if part[N][y] > 0:
			print(y, part[N][y])
