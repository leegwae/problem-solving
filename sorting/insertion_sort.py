def insertion_sort():
	for i in range(1, N):
		key = arr[i]
		prev = i - 1
		while prev >= 0 and arr[prev] > key:
			arr[prev + 1] = arr[prev]
			prev -= 1
		arr[prev + 1] = key


if __name__ == '__main__':
	arr = [4, 5, 2, 1]
	N = len(arr)
	insertion_sort()
	print(arr)
