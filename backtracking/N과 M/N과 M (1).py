# 수열
import sys

input = sys.stdin.readline


# def dfs(visited):
# 	if len(visited) == M:
# 		print(*visited, sep=" ")
# 		return
#
# 	for nxt in range(1, N + 1):
# 		if nxt not in visited:
# 			dfs([*visited, nxt])


def dfs():
	if len(ans) == M:
		print(*ans, sep=' ')
		return

	for num in range(1, N + 1):
		if num not in ans:
			ans.append(num)
			dfs()
			ans.pop()


if __name__ == '__main__':
	N, M = map(int, input().split())
	ans = []
	dfs()
