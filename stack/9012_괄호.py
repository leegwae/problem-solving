import sys

input = sys.stdin.readline


def is_vps(s: str) -> bool:
	if len(s) % 2 != 0:
		return False

	stack = []

	for p in s:
		if p == '(':
			stack.append(p)
		elif not stack or stack.pop() != '(':
			return False

	return not stack


for _ in range(int(input())):
	print('YES' if is_vps(input().strip()) else 'NO')
