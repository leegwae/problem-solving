import sys


input = sys.stdin.readline

# f(day, coupon) = (
#   f(day + 1, coupon - 3), (쿠폰 3장 사용)
# 	f(day + 1, coupon) + 10000, (1일권 사용)
# 	f(day + 3, coupon + 1) + 25000, (2일권 사용)
# 	f(day + 5, coupon + 2) + 37000, (3일권 사용)
# )


def f(day: int, coupon: int) -> int:
	if day > N:
		return 0

	if dp[day][coupon] != -1:
		return dp[day][coupon]

	if use[day] == 0:
		result = f(day + 1, coupon)
	else:
		result = min(
			f(day + 1, coupon) + 10000,
			f(day + 3, coupon + 1) + 25000,
			f(day + 5, coupon + 2) + 37000
		)

		if coupon >= 3:
			result = min(result, f(day + 1, coupon - 3))

	dp[day][coupon] = result
	return result


if __name__ == '__main__':
	N, M = map(int, input().split())
	use = [1] * (N + 1)
	if M > 0:
		for m in map(int, input().split()):
			use[m] = 0

	dp = [[-1] * (N + 1) for _ in range(N + 1)]
	answer = f(1, 0)
	print(answer)
