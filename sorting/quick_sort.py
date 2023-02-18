# def partition(left, right):
# 	pivot = arr[right]
# 	pos = left
# 	for i in range(left, right):
# 		if arr[i] <= pivot:
# 			arr[pos], arr[i] = arr[i], arr[pos]
# 			pos = pos + 1
#
# 	arr[pos], arr[right] = arr[right], arr[pos]
# 	return pos

def partition(left, right):
	low = left + 1
	high = right
	pivot = arr[left]

	while low <= high:
		while low <= right and arr[low] <= pivot:
			low += 1
		while high >= left and arr[high] > pivot:
			high -= 1

		if low <= high:
			arr[low], arr[high] = arr[high], arr[low]

	arr[left], arr[high] = arr[high], arr[left]
	return high


def quick_sort(left, right):
	if left < right:
		pivot_idx = partition(left, right)
		quick_sort(left, pivot_idx - 1)
		quick_sort(pivot_idx + 1, right)


if __name__ == '__main__':
	arr = [4, 3, 6, 1, 5, 4]
	quick_sort(0, len(arr) - 1)
	print(arr)
