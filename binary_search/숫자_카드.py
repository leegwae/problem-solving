import sys

input = sys.stdin.readline


def binary_search(target):
	left, right = 0, len(A) - 1

	while left <= right:
		mid = (left + right) // 2

		if target == A[mid]:
			return mid

		if target < A[mid]:
			right = mid - 1
		else:
			left = mid + 1

	return -1


if __name__ == '__main__':
	N = int(input())
	A = list(map(int, input().split()))	# 상근이가 가진 거
	M = int(input())
	B = list(map(int, input().split())) # 상근이가 가지고 있는가?

	A.sort()
	for i in B:
		print(1 if binary_search(i) != -1 else 0, end=' ')