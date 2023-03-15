import sys

input = sys.stdin.readline


def f(start, end, cnt):
	if start >= end or cnt == len(S):
		return

	m = S.find(min(S[start:end]), start, end)
	printed[m] = 1

	for i in range(len(S)):
		if printed[i]:
			print(S[i], end='')
	print()

	f(m+1, end, cnt + 1)
	f(start, m, cnt + 1)


if __name__ == '__main__':
	S = input().rstrip()
	printed = [0] * len(S)
	f(0, len(S), 0)
