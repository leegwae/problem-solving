import sys
import re


input = sys.stdin.readline

if __name__ == '__main__':
	p = re.compile('^[A-F]?A+F+C+[A-F]?$')

	T = int(input())
	for _ in range(T):
		s = input()
		print('Infected!' if p.match(s) else 'Good')
