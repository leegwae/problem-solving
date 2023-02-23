import sys

input = sys.stdin.readline


if __name__ == '__main__':
	N = int(input())
	crane = list(map(int, input().split()))
	M = int(input())
	box = list(map(int, input().split()))

	crane.sort(reverse=True)
	box.sort(reverse=True)

	if crane[0] < box[0]:
		print(-1)
		exit(0)

	answer = 0

	while box:
		for c in crane:
			if not box:
				break
			if box[-1] <= c:
				for j in range(len(box)):
					if box[j] <= c:
						box.pop(j)
						break
		answer += 1

	print(answer)
