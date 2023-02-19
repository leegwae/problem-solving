import sys

input = sys.stdin.readline


def permutation(l):
	N = len(l)
	per = []
	visited = [0] * N
	path = []

	def dfs():
		if len(path) == N:
			per.append(list(path))
			return

		for i in range(N):
			if visited[i] == 0:
				visited[i] = 1
				path.append(l[i])
				dfs()
				visited[i] = 0
				path.pop()

	dfs()
	return per


def combination(l, cnt):
	com = []
	path = []

	def dfs(cur):
		if len(path) == cnt:
			com.append(list(path))
			return

		if cur >= len(l):
			return

		path.append(l[cur])
		dfs(cur + 1)
		path.pop()
		dfs(cur + 1)

	dfs(0)

	return com


if __name__ == '__main__':
	N = int(input())
	x = list(map(int, input().split()))
	P, Q = map(int, input().split())

	if Q == 0:
		print(sum(x))
		exit(0)

	nums = permutation(x)
	ops = combination(list(range(P + Q)), Q)

	answer = 0
	for per in nums:
		for com in ops:
			result = 0
			for i in range(Q):
				if i == 0:
					result = sum(per[:com[i] + 1])
				else:
					result *= sum(per[com[i-1]+1:com[i]+1])
			result *= sum(per[com[-1]+1:])
			answer = max(answer, result)

	print(answer)
