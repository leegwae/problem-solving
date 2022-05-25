import sys

input = sys.stdin.readline


def get_max_count() -> int:
	meeting.sort(key=lambda x: (x[1], x[0]))

	result = 0
	prev = 0
	for m in meeting:
		start, end = m
		if start >= prev:
			result += 1
			prev = end

	return result


if __name__ == '__main__':
	N = int(input())
	meeting = [tuple(map(int, input().split())) for _ in range(N)]
	answer = get_max_count()
	print(answer)
