import sys

input = sys.stdin.readline
MAX_H = 1000000000

if __name__ == '__main__':
	N, M = map(int, input().split())
	tree = list(map(int, input().split()))
	left, right = 1, MAX_H
	H = 0
	while True:
		if left > right:
			break

		middle = (left + right) // 2

		total = 0
		for t in tree:
			if t > middle:
				total += t - middle

		if total < M:
			right = middle - 1
		elif total >= M:
			H = max(H, middle)
			left = middle + 1

	print(H)
