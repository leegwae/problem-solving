def bubble_sort():
	for last in range(N - 1, 0, -1):
		for i in range(0, last):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]


if __name__ == '__main__':
	arr = [4, 5, 2, 1]
	N = len(arr)
	bubble_sort()
	print(arr)
