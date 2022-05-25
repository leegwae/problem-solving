import sys
import heapq

input = sys.stdin.readline


def compare():
	heapq.heapify(card)
	result = 0

	while len(card) > 1:
		A, B = heapq.heappop(card), heapq.heappop(card)
		cnt = A + B
		result += cnt
		heapq.heappush(card, cnt)

	return result


if __name__ == '__main__':
	N = int(input())
	card = [int(input()) for _ in range(N)]

	answer = compare()
	print(answer)