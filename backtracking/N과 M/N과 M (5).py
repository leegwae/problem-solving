import sys

input = sys.stdin.readline


def dfs():
	if len(ans) == M:
		print(*ans, sep=' ')

	for num in nums:
		if num not in ans:
			ans.append(num)
			dfs()
			ans.pop()


if __name__ == '__main__':
	N, M = map(int, input().split())
	nums = list(map(int, input().split()))
	nums.sort()
	ans = []
	dfs()
