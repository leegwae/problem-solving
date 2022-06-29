def partition(left, right):
	pivot = arr[right]
	i = left - 1
	for j in range(left, right):
		if arr[j] <= pivot:
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[right] = arr[right], arr[i + 1]

	return i + 1


def quick_sort(left, right):
	if left < right:
		pivot = partition(left, right)
		quick_sort(left, pivot - 1)
		quick_sort(pivot + 1, right)


if __name__ == '__main__':
	arr = [4, 3, 6, 1, 5, 4]
	quick_sort(0, len(arr) - 1)
	print(arr)
