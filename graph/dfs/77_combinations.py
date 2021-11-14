from typing import List


class Solution:
	def combine(self, n: int, k: int) -> List[List[int]]:
		def dfs(prev, remain):
			if len(prev) == k:
				result.append(prev)
				return

			for nxt in remain:
				p = prev + [nxt]
				r = list(filter(lambda x: x not in p, range(nxt + 1, n + 1)))

				dfs(p, r)
		result = []
		for i in range(1, n + 1):
			dfs([i], range(i + 1, n + 1))
		return result


if __name__ == '__main__':
	s = Solution()
	n, k = 3, 3
	print(s.combine(n, k))
