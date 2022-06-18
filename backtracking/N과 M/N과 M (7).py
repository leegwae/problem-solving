import sys

input = sys.stdin.readline


def dfs():
	if len(ans) == M:
		print(*ans, sep=' ')
		return

	for num in nums:
		ans.append(num)
		dfs()
		ans.pop()


if __name__ == '__main__':
	N, M = map(int, input().split())
	nums = list(map(int, input().split()))
	nums.sort()
	ans = []
	dfs()
