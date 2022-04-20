from typing import List


def calculate_prefix_sum(matrix: List[List[int]], n) -> None:
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			matrix[i][j] += matrix[i][j-1] + matrix[i-1][j] - matrix[i-1][j-1]


if __name__ == '__main__':

	N, M = list(map(int, input().split()))
	arr = [[0] * (N + 1)]
	scopes = []

	for i in range(1, N + 1):
		arr.append([0] + list(map(int, input().split())))

	calculate_prefix_sum(arr, N)

	for i in range(M):
		scopes.append(list(map(int, input().split())))

	for x1, y1, x2, y2 in scopes:
		print(arr[x2][y2] - (arr[x2][y1-1] + arr[x1-1][y2] - arr[x1-1][y1-1]))
