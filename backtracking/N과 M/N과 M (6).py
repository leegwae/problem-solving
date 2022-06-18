import sys

input = sys.stdin.readline


def dfs(i):
	if len(ans) == M:
		print(*ans, sep=' ')
		return

	if i == N:
		return

	ans.append(nums[i])
	dfs(i + 1)
	ans.pop()
	dfs(i + 1)


if __name__ == '__main__':
	N, M = map(int, input().split())
	nums = list(map(int, input().split()))
	nums.sort()
	ans = []
	dfs(0)
