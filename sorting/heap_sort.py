from typing import List


def heap_sort(arr: List[int]):
	def heapify(size, idx):
		largest = idx
		left = 2 * idx + 1
		right = 2 * idx + 2

		if left < size and arr[largest] < arr[left]:
			largest = left

		if right < size and arr[largest] < arr[right]:
			largest = right

		if largest != idx:
			arr[idx], arr[largest] = arr[largest], arr[idx]
			heapify(size, largest)

	N = len(arr)
	for i in range(N // 2 - 1, -1, -1):
		heapify(N, i)

	for i in range(N - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(i, 0)
