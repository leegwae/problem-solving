import sys

input = sys.stdin.readline


def get_min_count():
	coins.reverse()
	k = K
	i = 0
	count = 0

	while k > 0 and i < N:
		if k >= coins[i]:
			count += k // coins[i]
			k %= coins[i]
		i += 1

	return count


if __name__ == '__main__':
	N, K = map(int, input().split())
	coins = [int(input()) for _ in range(N)]
	answer = get_min_count()
	print(answer)
