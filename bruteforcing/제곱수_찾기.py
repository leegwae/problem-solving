import sys

input = sys.stdin.readline


def perfectsqure(x: int):
	return int(x ** 0.5) ** 2 == x


if __name__ == '__main__':
	N, M = map(int, input().split())
	ticket = [list(input().rstrip()) for _ in range(N)]

	answer = -1

	if N == 1 and M == 1 and perfectsqure(int(ticket[0][0])):
		print(ticket[0][0])
		exit(0)

	for i in range(N):
		for j in range(M):
			for n in range(N):
				for m in range(M):
					if n == 0 and m == 0:
						continue
					seq = ''
					a, b = i, j
					while a < N and b < M:
						seq += ticket[a][b]

						if perfectsqure(int(seq)):
							answer = max(answer, int(seq))
						if perfectsqure(int(seq[::-1])):
							answer = max(answer, int(seq[::-1]))
						a += n
						b += m

					seq = ''
					a, b = i, j
					while a < N and b >= 0:
						seq += ticket[a][b]
						if perfectsqure(int(seq)):
							answer = max(answer, int(seq))
						if perfectsqure(int(seq[::-1])):
							answer = max(answer, int(seq[::-1]))
						a += n
						b -= m

	print(answer)
