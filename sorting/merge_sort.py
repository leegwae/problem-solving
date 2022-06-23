def merge_sort(left: int, right: int) -> None:
	if left >= right:
		return

	middle = (left + right) // 2
	merge_sort(left, middle)
	merge_sort(middle + 1, right)
	merge(left, middle, right)


def merge(left: int, middle: int, right: int) -> None:
	i = left
	j = middle + 1
	k = left

	while i <= middle and j <= right:
		if arr[i] <= arr[j]:
			sorted[k] = arr[i]
			k += 1
			i += 1
		else:
			sorted[k] = arr[j]
			k += 1
			j += 1

	while i <= middle:
		sorted[k] = arr[i]
		i += 1
		k += 1

	while j <= right:
		sorted[k] = arr[j]
		j += 1
		k += 1

	for i in range(left, right + 1):
		arr[i] = sorted[i]


if __name__ == '__main__':
	arr = [4, 5, 2, 1]
	N = len(arr)
	sorted = [0] * N
	merge_sort(0, N - 1)
	print(arr)
