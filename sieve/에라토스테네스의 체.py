import sys

input = sys.stdin.readline


def eratosthenes():
	cnt = 0

	for i in range(2, N + 1):
		for j in range(i, N + 1, i):
			if isPrime[j]:
				isPrime[j] = False
				cnt += 1

				if cnt == K:
					return j


if __name__ == '__main__':
	N, K = map(int, input().split())
	isPrime = [True] * (N + 1)
	isPrime[0] = isPrime[1] = False

	answer = eratosthenes()
	print(answer)