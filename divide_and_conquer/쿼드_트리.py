import sys

input = sys.stdin.readline


def compress(y, x, n):
	if n == 1:
		return M[y][x]

	nn = n // 2
	m1 = compress(y, x, nn)
	m2 = compress(y, x + nn, nn)
	m3 = compress(y + nn, x, nn)
	m4 = compress(y + nn, x + nn, nn)

	if m1 == m2 == m3 == m4 and len(m1) == 1:
		return m1

	return f'({m1 + m2 + m3 + m4})'


if __name__ == "__main__":
	N = int(input())
	M = [list(input().rstrip()) for _ in range(N)]
	answer = compress(0, 0, N)
	print(answer)
