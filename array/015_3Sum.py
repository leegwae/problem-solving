class Solution:
    # n^3
    # def threeSum(self, nums: list[int]) -> list[list[int]]:
    #     def threeSumWithTarget(target: int, numbers: list[int]) -> list[list[int]]:
    #         if not len(numbers) >= 2:
    #             return []
    #
    #         left, right = 0, len(numbers) - 1
    #         threeSum_lists = []
    #         numbers.sort()
    #
    #         while not left >= right:
    #             if numbers[left] + numbers[right] == target:
    #                 threeSum_list = [numbers[left], numbers[right], -target]
    #                 threeSum_list.sort()
    #                 if threeSum_list not in threeSum_lists:
    #                     threeSum_lists.append(threeSum_list)
    #                 left += 1
    #                 right -= 1
    #             elif numbers[left] + numbers[right] > target:
    #                 right -= 1
    #             else:
    #                 left += 1
    #
    #         return threeSum_lists
    #
    #     num_sets = set(nums)
    #     threeSum_lists = []
    #
    #     for i, num in enumerate(num_sets):
    #         copied = nums.copy()
    #         copied.remove(num)
    #         sub_lists = threeSumWithTarget(0 - num, copied)
    #
    #         for sub_list in sub_lists:
    #             if sub_list not in threeSum_lists:
    #                 threeSum_lists.append(sub_list)
    #
    #     threeSum_lists.sort()
    #
    #     return threeSum_lists

    # two pointer
    # n^2
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):

            # 리스트가 정렬되어 있으므로,
            # 반복된 요소들은 건너뛴다.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result = [nums[i], nums[left], nums[right]]
                    results.append(result)

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        results.sort()

        return results


if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,1,2,-1,-1, -1]
    print(s.threeSum(nums))