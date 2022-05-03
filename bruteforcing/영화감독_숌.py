import sys

input = sys.stdin.readline

N = int(input())

loop = 1
num = 666

while True:
	if loop == N:
		break

	num += 1

	if str(num).find('666') != -1:
		loop += 1


print(num)