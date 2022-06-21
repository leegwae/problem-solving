import sys

input = sys.stdin.readline


def sum(to):
	pos = to
	result = 0

	while pos > 0:
		result += tree[pos]
		pos -= (pos & -pos)

	return result


def update(at, diff):
	pos = at

	while pos < len(tree):
		tree[pos] += diff
		pos += (pos & -pos)


if __name__ == "__main__":
	N, M, K = map(int, input().split())
	arr = [0] * (N + 1)
	tree = [0] * (N + 1)
	for i in range(1, N + 1):
		el = int(input())
		update(i, el - arr[i])
		arr[i] = el

	for _ in range(M + K):
		a, b, c = map(int, input().split())
		if a == 1:
			diff = c - arr[b]
			update(b, diff)
			arr[b] = c
		elif a == 2:
			print(sum(c) - sum(b - 1))
