# 브루트 포스로 풀기
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 딕셔너리를 사용하기 풀이하기
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            nums_map[n] = i

        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums_map and i != nums_map[complement]:
                return [i, nums_map[complement]]

# 조회 구조 개선
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums_map:
                return [nums_map[complement], i]

            nums_map[n] = i