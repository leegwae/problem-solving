import sys

input = sys.stdin.readline


if __name__ == '__main__':
	S = input()
	T = input()

	while len(T) > len(S):
		if T[-1] == 'A':
			T = T[:-1]
		else:
			T = T[:-1][::-1]
	print(int(T == S))
