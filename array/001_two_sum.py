
class Solution:

    # 브루트 포스로 풀기
    # n^2
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    # 딕셔너리를 사용하기 풀이하기
    # n
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     nums_map = {}
    #     for i, n in enumerate(nums):
    #         nums_map[n] = i
    #
    #     for i, n in enumerate(nums):
    #         complement = target - n
    #
    #         if complement in nums_map and i != nums_map[complement]:
    #             return [i, nums_map[complement]]

    # 투 포인터 사용하기
    # 요소가 정렬된 경우 사용 가능
    # n
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_list = [(i, n) for (i, n) in enumerate(nums)]
        nums_list.sort(key=lambda x: x[1])

        left, right = 0, len(nums_list) - 1
        while not left == right:
            total = nums_list[left][1] + nums_list[right][1]

            if total > target:
                right -= 1
            elif total < target:
                left += 1
            elif total == target:
                return [nums_list[left][0], nums_list[right][0]]


if __name__ == '__main__':
    s = Solution()
    nums = [3,2,3]
    target = 6
    print(s.twoSum(nums, target))