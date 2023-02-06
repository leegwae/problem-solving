import sys

input = sys.stdin.readline

if __name__ == '__main__':
	N = int(input())
	B = list(map(int, input().split()))
	answer = 0
	while sum(B) != 0:
		for i in range(N):
			if B[i] % 2 == 1:
				B[i] -= 1
				answer += 1

		zero = True
		for i in range(N):
			if B[i] != 0:
				zero = False
			B[i] //= 2

		if zero:
			break

		answer += 1
	print(answer)
