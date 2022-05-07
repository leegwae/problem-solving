import sys

input = sys.stdin.readline

MIN_VOWELS, MIN_CONSONANT = 1, 2
VOWELS = set('a, e, i, o, u'.split(', '))


def get_vowels_count(s: str) -> int:
	count = 0
	for ch in s:
		if ch in VOWELS:
			count += 1

	return count


def get_letter_combinations(acc, pos):
	if len(acc) == L:
		count_v = get_vowels_count(acc)
		if count_v >= MIN_VOWELS and len(acc) - count_v >= MIN_CONSONANT:
			print(acc)
		return

	if pos == C:
		return

	get_letter_combinations(acc + characters[pos], pos + 1)
	get_letter_combinations(acc, pos + 1)


if __name__ == '__main__':
	L, C = map(int, input().split())
	characters = sorted(list(input().split()))
	get_letter_combinations('', 0)

