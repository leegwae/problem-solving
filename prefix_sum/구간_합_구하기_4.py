from typing import List

n, m = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
scopes = []

for i in range(m):
	scopes.append(list(map(int, input().split())))


def fun_get_prefix_sum(arr: List[int], pos: int) -> List[int]:
	if pos == len(arr):
		return arr

	if pos != 0:
		arr[pos] += arr[pos-1]

	return fun_get_prefix_sum(arr, pos + 1)


def get_prefix_sum(arr: List[int]) -> None:
	fun_get_prefix_sum(arr, 0)


get_prefix_sum(numbers)

for [a, b] in scopes:
	print(numbers[b] - numbers[a - 1])