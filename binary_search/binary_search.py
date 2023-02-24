import bisect


def binary_search_recursion(left, right):
	if left > right:
		return -1

	middle = (left + right) // 2

	if M[middle] == N:
		return middle
	elif M[middle] < N:
		return binary_search_recursion(middle + 1, right)
	elif M[middle] > N:
		return binary_search_recursion(left, middle - 1)


def binary_search_iteration():
	left, right = 0, len(M) - 1

	while left <= right:
		middle = (left + right) // 2

		if M[middle] == N:
			return middle

		if M[middle] < N:
			left = middle + 1
		elif M[middle] > N:
			right = middle - 1

	return -1


def binary_search():
	idx = bisect.bisect_left(M, N)

	if idx < len(M) and M[idx] == N:
		return idx
	else:
		return -1


if __name__ == '__main__':
	N = int(input('탐색할 요소를 입력하세요 '))
	M = list(map(int, input('리스트를 입력하세요. 예)1 2 3 4 5' ).split()))
	print(f'재귀: {binary_search_recursion(0, len(M) - 1)}')
	print(f'반복: {binary_search_iteration()}')
	print(f'내장 모듈: {binary_search()}')
