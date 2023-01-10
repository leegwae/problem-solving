import sys

input = sys.stdin.readline

if __name__ == '__main__':
	# 마을 수, 트럭 용량
	N, C = map(int, input().split())
	M = int(input())
	# (출발, 도착, 개수)
	arr = [tuple(map(int, input().split())) for _ in range(M)]

	arr.sort(key=lambda x: (x[1], x[0]))

	answer = 0
	capacity = [0] * (N + 1)
	for a, b, cnt in arr:
		c = min(cnt, C - max(capacity[a:b]))
		for i in range(a, b):
			capacity[i] += c
		answer += c
	print(answer)
