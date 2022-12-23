import sys
import collections

input = sys.stdin.readline


if __name__ == '__main__':
	d = collections.deque(input().strip())

	answer = len(d)

	is_palindrome = True
	all_same = True
	while len(d) > 1:
		left, right = d.popleft(), d.pop()
		if left != right:
			is_palindrome = False
			break
		if len(d) >= 1 and left != d[0]:
			all_same = False

	if not is_palindrome:
		print(answer)
	else:
		if all_same:
			print(-1)
		else:
			print(answer - 1)
