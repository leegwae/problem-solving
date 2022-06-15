import sys
from bisect import bisect_left

input = sys.stdin.readline


def len_lis() -> int:
	M = []
	for cur in range(N):
		pos = bisect_left(M, A[cur])
		if len(M) == pos:
			M.append(A[cur])
		else:
			M[pos] = A[cur]

	return len(M)


if __name__ == '__main__':
	N = int(input())
	A = list(map(int, input().split()))
	answer = len_lis()
	print(answer)
