class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()

        return sum(nums[::2])

if __name__ == '__main__':
    s = Solution()
    nums = [6,2,6,5,1,2]
    print(s.arrayPairSum(nums))