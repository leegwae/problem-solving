import sys

input = sys.stdin.readline

N = int(input())
candy = [list(input().strip()) for _ in range(N)]

dy = [-1, 0]
dx = [0, 1]


def get_eatable_candy_count() -> int:
	m_count = 0
	r_cur, c_cur = 1, 1

	for i in range(N):
		for j in range(1, N):
			if candy[i][j - 1] == candy[i][j]:
				r_cur += 1
			else:
				m_count = max(m_count, r_cur)
				r_cur = 1

			if candy[j - 1][i] == candy[j][i]:
				c_cur += 1
			else:
				m_count = max(m_count, c_cur)
				c_cur = 1

		m_count = max(m_count, r_cur, c_cur)
		r_cur, c_cur = 1, 1

	return m_count


max_count = 0
for y in range(N):
	for x in range(N):
		for i in range(2):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= ny <= N - 1 and 0 <= nx <= N - 1:
				if candy[y][x] != candy[ny][nx]:
					candy[y][x], candy[ny][nx] = candy[ny][nx], candy[y][x]
					max_count = max(max_count, get_eatable_candy_count())
					candy[y][x], candy[ny][nx] = candy[ny][nx], candy[y][x]

print(max_count)