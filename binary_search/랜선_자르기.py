import sys

input = sys.stdin.readline

if __name__ == '__main__':
	K, N = map(int, input().split())
	arr = [int(input()) for _ in range(K)]

	arr.sort()
	left, right = 1, max(arr)
	while left <= right:
		mid = (left + right) // 2

		cnt = 0
		for length in arr:
			cnt += length // mid

		if cnt >= N:
			left = mid + 1
		else:
			right = mid - 1
	print(left-1)
