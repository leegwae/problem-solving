import sys

input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))


def dfs(acc: int, pos: int):
	global count
	if pos == N:
		return 0

	if (acc + numbers[pos]) == S:
		count += 1

	dfs(acc + numbers[pos], pos + 1)
	dfs(acc, pos + 1)


if __name__ == '__main__':
	count = 0
	dfs(0, 0)
	print(count)
