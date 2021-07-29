from functools import reduce
class Solution:
    # n^2
    # def productExceptSelf(self, nums: list[int]) -> list[int]:
    #
    #     result = []
    #     for num in nums:
    #         copied = nums.copy()
    #         copied.remove(num)
    #
    #         mul = reduce(lambda x, y: x * y, copied)
    #         result.append(mul)
    #
    #     return result

    # using pow
    # def productExceptSelf(self, nums: list[int]) -> list[int]:
    #     def multipleWithoutTarget(index: int) -> int:
    #         result = 1
    #
    #         for i, n in enumerate(nums):
    #             if not i == index:
    #                 result *= n
    #
    #         return result
    #
    #     # 요소에 0이 없다면 요소 전부를 곱한 것에서 각각의 값을 나눈다.
    #     # 요소에 0이 한 개 이면 해당 0이 있는 인덱스를 제외하고 0이다.
    #     # 요소에 0이 두 개 이상이면 전부 0이다.
    #     countzero = nums.count(0)
    #
    #     if countzero >= 2:
    #         return [0] * len(nums)
    #     elif countzero == 1:
    #         index = nums.index(0)
    #         results = [0] * len(nums)
    #         results[index] = multipleWithoutTarget(index)
    #         return results;
    #     elif countzero == 0:
    #         mul = multipleWithoutTarget(-1)
    #         return [int(mul * pow(num, -1)) for num in nums]

    # n
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = []
        p = 1
        size = len(nums)
        for i in range(0, size):
            output.append(p)
            p *= nums[i]    

        p = 1
        for i in range(size - 1, -1, -1):
            output[i] *= p
            p *= nums[i]

        return output


if __name__ == '__main__':
    s = Solution()
    nums = [-1,1,0,-3,3]
    print(s.productExceptSelf(nums))