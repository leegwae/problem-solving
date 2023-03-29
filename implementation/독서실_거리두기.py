import sys

input = sys.stdin.readline


def time(hhmm):
	h = hhmm // 100
	m = hhmm % 100
	return h, m


def minute(h, m):
	return h * 60 + m


def seat(it):
	s = 0
	dist = 0
	for i in range(N):
		if timetable[it][i] == 1:
			continue
		d = int(1e09)
		for j in range(N):
			if i == j or timetable[it][j] == 0:
				continue
			d = min(d, abs(j - i))
		if d > dist:
			dist = d
			s = i
	return s


if __name__ == '__main__':
	N, T, P = map(int, input().split())
	S, E = minute(*time(900)), minute(*time(2100))
	reservation = []
	for _ in range(T):
		it, ot = map(int, input().split())
		it, ot = minute(*time(it)), minute(*time(ot))
		reservation.append((it-S, ot-S))
	reservation.sort()

	timetable = [[0] * N for _ in range(E-S+1)]
	for it, ot in reservation:
		s = seat(it)
		for t in range(it, ot):
			timetable[t][s] = 1

	answer = 0
	for i in range(E-S):
		answer += int(not timetable[i][P-1])
	print(answer)