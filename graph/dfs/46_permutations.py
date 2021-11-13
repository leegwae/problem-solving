from typing import List
import itertools


class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		def dfs(prev, remain):
			if len(remain) == 0:
				result.append(prev)
				return

			for nxt in remain:
				p = prev + [nxt]
				r = list(filter(lambda x: x not in p, remain))
				dfs(p, r)

		result = []

		for num in nums:
			dfs([num], list(filter(lambda x: x != num, nums)))

		return result

	def permute(self, nums: List[int]) -> List[List[int]]:
		return list(map(list, itertools.permutations(nums)))


if __name__ == "__main__":
	s = Solution()
	nums = [1]
	print(s.permute(nums))
