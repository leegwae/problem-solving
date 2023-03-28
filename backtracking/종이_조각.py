import sys

input = sys.stdin.readline


def get_sum():
	total = 0
	for i in range(N):
		piece = 0
		for j in range(M):
			if visited[(i * M) + j] == 1:
				piece = (piece * 10) + int(paper[i][j])
			else:
				total += piece
				piece = 0
		total += piece

	for i in range(M):
		piece = 0
		for j in range(N):
			if visited[(j * M) + i] == 0:
				piece = (piece * 10) + int(paper[j][i])
			else:
				total += piece
				piece = 0
		total += piece

	return total


def backtracking(cur):
	global result
	if cur == (N * M):
		result = max(result, get_sum())
		return

	visited[cur] = 1
	backtracking(cur + 1)
	visited[cur] = 0
	backtracking(cur + 1)


if __name__ == '__main__':
	N, M = map(int, input().split())
	paper = [list(input().rstrip()) for _ in range(N)]
	visited = [0] * (N * M)
	result = 0
	backtracking(0)
	print(result)
