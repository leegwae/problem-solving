import sys

input = sys.stdin.readline


if __name__ == '__main__':
	H, W = map(int, input().split())
	height = list(map(int, input().split()))

	if W >= 3 and height[0] == height[-1] == max(height):
		print(sum(map(lambda x: height[0]-x, height)))
		exit(0)

	answer = 0
	a, b = 0, 0
	while True:
		while a + 1 < W and height[a] <= height[a + 1]:
			a += 1
		b = a + 2
		while b < W and height[b] < height[a]:
			b += 1
		if a + 1 < W and b == W:
			b = height.index(max(height[a + 1:]), a + 1)
		if a < W and b < W:
			h = min(height[a], height[b])
			for i in range(a + 1, b):
				answer += h - height[i]
			a = b
		else:
			break
	print(answer)
