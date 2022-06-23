def selection_sort():
	for start in range(0, N - 1):
		least = start
		for i in range(start + 1, N):
			if arr[least] > arr[i]:
				least = i

		arr[start], arr[least] = arr[least], arr[start]


if __name__ == '__main__':
	arr = [4, 5, 2, 1]
	N = len(arr)
	selection_sort()
	print(arr)
