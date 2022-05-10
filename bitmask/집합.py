import sys

input = sys.stdin.readline

MAX_SIZE = 20


def add(x):
	global S
	if not includes(x):
		S |= (1 << x)


def remove(x):
	global S
	if includes(x):
		S &= ~(1 << x)


def includes(x):
	global S
	return (S & (1 << x)) != 0


def check(x):
	print(1 if includes(x) else 0)


def toggle(x):
	global S
	S ^= (1 << x)


def all():
	global S
	S = (1 << (MAX_SIZE + 1)) - 1


def empty():
	global S
	S = 0


if __name__ == '__main__':
	M = int(input())
	S = 0
	for _ in range(M):
		raw = input().split()
		if len(raw) == 1:
			fun = raw[0]
			locals()[fun]()
		else:
			fun, param = raw
			locals()[fun](int(param))
