import sys

input = sys.stdin.readline

if __name__ == '__main__':
	N = int(input())
	arr = list(map(int, input().split()))
	arr.sort()

	if arr[-1] < 0:
		print(arr[-1], arr[-2])
	elif arr[0] > 0:
		print(arr[0], arr[1])
	else:
		pass