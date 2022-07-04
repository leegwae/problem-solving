def eratosthenes():
	for i in range(2, sqrtN):
		if isPrime[i]:
			for j in range(i * i, N + 1, i):
				isPrime[j] = False


if __name__ == '__main__':
	N = int(input())
	isPrime = [True] * (N + 1)
	sqrtN = int(N ** (1 / 2))
	eratosthenes()
	print(list(filter(lambda i: isPrime[i], range(2, N + 1))))
