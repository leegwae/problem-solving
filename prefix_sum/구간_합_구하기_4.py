import sys
from typing import List


def fun_get_prefix_sum(arr: List[int], pos: int) -> List[int]:
	if pos == len(arr):
		return arr

	if pos != 0:
		arr[pos] += arr[pos-1]

	return fun_get_prefix_sum(arr, pos + 1)


def get_prefix_sum_recursion(arr: List[int]) -> None:
	fun_get_prefix_sum(arr, 0)


def get_prefix_sum(arr: List[int]) -> None:
	for i in range(1, len(arr)):
		arr[i] += arr[i-1]


if __name__ == '__main__':
	n, m = map(int, sys.stdin.readline().split())
	numbers = [0] + list(map(int, sys.stdin.readline().split()))
	scopes = []

	for i in range(m):
		scopes.append(list(map(int, sys.stdin.readline().split())))

	get_prefix_sum(numbers)

	for [a, b] in scopes:
		print(numbers[b] - numbers[a - 1])