import sys

input = sys.stdin.readline
INF = 1000000000


if __name__ == '__main__':
	N = int(input())
	line = [tuple(map(int, input().split())) for _ in range(N)]
	line.sort(key=lambda x: x[0])

	total = 0
	px, py = -INF, -INF
	for cx, cy in line:
		if py < cx:
			total += py - px
			px, py = cx, cy
		else:
			py = max(py, cy)
	total += py - px
	print(total)
