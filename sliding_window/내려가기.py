# PyPy3 통과
import sys

input = sys.stdin.readline


if __name__ == "__main__":
	N = int(input())
	M = [list(map(int, input().split())) for _ in range(N)]
	max_dp, min_dp = [0] * 3, [0] * 3
	for r in range(N):
		m0, m1, m2 = max_dp
		max_dp = [
			max(m0, m1) + M[r][0],
			max(m0, m1, m2) + M[r][1],
			max(m1, m2) + M[r][2]
		]

		m0, m1, m2 = min_dp
		min_dp = [
			min(m0, m1) + M[r][0],
			min(m0, m1, m2) + M[r][1],
			min(m1, m2) + M[r][2]
		]
	print(max(max_dp), min(min_dp))
