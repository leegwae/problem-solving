import sys

input = sys.stdin.readline


sys.setrecursionlimit(1000000)

# 자릿수가 pos개이고 start로 시작하는 감소하는 수를 cur에 넣는다.
def f(pos: int, start: str):
	global cur, prev, cnt
	# 감소하는 수의 자릿수는 11개가 될 수 없다. 10개가 최대이다.
	if pos == 11:
		print(-1)
		exit(0)

	# 수는 10으로 시작할 수 없다. 9가 최대이다.
	# 따라서 다음 자릿수 pos + 1개일 때의 감소하는 수를 구해야하는데,
	# 자릿수가 A개일 때 가장 작은 수는 A-1부터 시작하므로
	# 자릿수가 pos + 1개이고 pos로 시작하는 감소하는 수를 찾으러 간다.
	if int(start) == 10:
		prev = cur
		cur = []
		f(pos + 1, str(pos))

	# prev: 자릿수가 pos-1개인 감소하는 수들
	# cur: 자릿수가 pos개인 감수하는 수들
	# 자릿수가 P개이고 Q로 시작하는 감소하는 수는
	# Q + 자릿수가 P-1개이고 0,..., Q-1로 시작하는 감소하는 수이다.
	for n in prev:
		if int(n[0]) >= int(start):
			break
		e = start + n
		cur.append(e)
		cnt += 1

		if cnt == N + 1:
			print(cur[-1])
			exit(0)

	# 자릿수가 pos개이고 start + 1로 시작하는 수를 찾으러 간다.
	f(pos, str(int(start) + 1))


if __name__ == '__main__':
	N = int(input())
	if N <= 10:
		print(N)
	else:
		prev = list(map(str, range(10)))
		cur = []
		cnt = len(prev)
		f(2, '1')

