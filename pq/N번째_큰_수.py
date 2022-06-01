import sys
import heapq

input = sys.stdin.readline

if __name__ == '__main__':
	N = int(input())
	M = list(map(int, input().split()))
	heapq.heapify(M)

	for i in range(N - 1):
		for n in list(map(int, input().split())):
			heapq.heappush(M, n)
			heapq.heappop(M)

	print(M[0])
