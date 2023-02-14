import sys

input = sys.stdin.readline

if __name__ == '__main__':
	N, M = map(int, input().split())
	times = list(map(int, input().split()))

	if N <= M:
		print(N)
		exit(0)

	# 모든 아이들이 탑승한 t(t>=0)분 구하기
	left, right = 1, N * max(times)
	while left < right:
		mid = (left + right) // 2

		children = 0
		for i in range(M):
			children += (mid // times[i]) + 1

		if children < N:
			left = mid + 1
		else:
			right = mid
	t = left

	# t-1분까지 탑승하는 아이들 수 구하기
	children = 0
	for i in range(M):
		children += ((t - 1) // times[i]) + 1

	# t분에 탑승하는 아이들 수 구하기
	remain = N - children

	# 마지막 아이가 탑승하는 놀이기구 번호 구하기
	for i in range(M):
		if t % times[i] == 0:
			remain -= 1
			if remain == 0:
				print(i + 1)
				exit(0)
