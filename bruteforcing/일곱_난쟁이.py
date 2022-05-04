import sys

input = sys.stdin.readline

dwarf = [int(input()) for _ in range(9)]
total = sum(dwarf)


def get_fake_dwarf():
	for i in range(8):
		for j in range(i + 1, 9):
			if total - dwarf[i] - dwarf[j] == 100:
				return [dwarf[i], dwarf[j]]


fake_dwarf = get_fake_dwarf()
print(*sorted([h for h in dwarf if h not in fake_dwarf]), sep="\n")
