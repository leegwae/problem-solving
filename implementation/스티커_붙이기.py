import sys
from typing import List, Tuple

input = sys.stdin.readline


# (y, x)에 스티커를 붙일 수 있는지 구하기
def attachable(y, x, sticker) -> bool:
	R, C = len(sticker), len(sticker[0])

	if y + R > N or x + C > M:
		return False

	for r in range(R):
		for c in range(C):
			if sticker[r][c] == 1 and board[y + r][x + c] == 1:
				return False

	return True


# 스티커를 붙일 수 있는 (y, x) 구하기
def get_pos(sticker) -> Tuple[int, int]:
	for y in range(N):
		for x in range(M):
			if attachable(y, x, sticker):
				return y, x

	return -1, -1


# (y, x)에 스티커 붙이기
def attach(y, x, sticker):
	R, C = len(sticker), len(sticker[0])

	for r in range(R):
		for c in range(C):
			if sticker[r][c] == 1:
				board[y + r][x + c] = 1


# 시계방향으로 스티커 90도 돌리기
def rotate(sticker) -> List[List[int]]:
	R, C = len(sticker), len(sticker[0])
	rotated = []

	for c in range(C):
		row = []
		for r in reversed(range(R)):
			row.append(sticker[r][c])
		rotated.append(row)

	return rotated


if __name__ == '__main__':
	N, M, K = map(int, input().split())
	board = [[0] * M for _ in range(N)]
	for _ in range(K):
		R, C = map(int, input().split())
		s = [list(map(int, input().split())) for _ in range(R)]

		for _ in range(4):
			pos = get_pos(s)
			if pos != (-1, -1):
				attach(*pos, s)
				break

			s = rotate(s)

	answer = 0
	for i in range(N):
		for j in range(M):
			if board[i][j] == 1:
				answer += 1
	print(answer)
