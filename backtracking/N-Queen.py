import sys

input = sys.stdin.readline


def check(y):
	for qy in range(y):
		if M[qy] == M[y] or abs(qy - y) == abs(M[y] - M[qy]):
			return False

	return True


def backtracking(y):
	global answer

	if y == N:
		answer += 1
		return

	for x in range(N):
		M[y] = x
		if check(y):
			backtracking(y + 1)


if __name__ == '__main__':
	N = int(input())
	answer = 0
	M = [-1] * N
	backtracking(0)
	print(answer)
