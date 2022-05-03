import sys

input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())

distance = 0
left, right = 1, M

for _ in range(J):
	pos = int(input())

	move = 0
	if pos < left:
		move = left - pos
		left, right = pos, right - move
	elif pos > right:
		move = pos - right
		left, right = left + move, pos
	distance += move

print(distance)