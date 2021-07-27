class Solution:
    # n^2
    # def trap(self, height: list[int]) -> int:
    #     def findHigherThanTarget(target: int, h: list[int]) -> int:
    #         for idx, n in enumerate(h):
    #             if n > target:
    #                 return idx
    #         return -1
    #
    #     water = 0
    #
    #     i = 1
    #
    #     if len(height) > 2:
    #         while not i == len(height) - 1:
    #             left = i - 1
    #
    #             # 왼쪽 벽이 현재 벽보다 높으면
    #             if height[left] > height[i]:
    #                 # 오른쪽 벽 중 왼쪽 벽보다 높거나 같은 벽의 인덱스 가져오기
    #                 right_index = findHigherThanTarget(height[left] - 1, height[i+1:]) + (i + 1)
    #
    #                 # 오른쪽 벽 중 왼쪽 벽보다 높거나 같은 벽이 있다면
    #                 if not right_index == i:
    #                     for j in range(i, right_index):
    #                         water += (height[left] - height[j])
    #                     i = right_index
    #                 else:  # 오른쪽 벽 중 왼쪽 벽보다 높거나 같은 벽이 없다면
    #                     # 오른쪽 벽 중 가장 높은 벽 가져오기
    #                     right_highest = max([(idx + (i + 1), n) for idx, n in enumerate(height[i+1:])],
    #                                         key=lambda x: x[1])
    #
    #                     # 오른쪽 벽 중 가장 높은 벽이 현재 벽보다 크거나 같으면
    #                     if right_highest[1] >= height[i]:
    #                         for j in range(i, right_highest[0]):
    #                             water += (right_highest[1] - height[j])
    #                         i = right_highest[0]
    #                     else:  # 오른쪽 벽 가장 높은 벽이 현재 벽보다 작으면
    #                         i += 1
    #             else:
    #                 i += 1
    #     return water

    # two pointer
    # n
    def trap(self, height: list[int]) -> int:

        if not len(height) > 2:
            return 0

        water = 0
        left, right = 0, len(height) - 1

        left_max, right_max = height[left], height[right]

        while left <= right:
            left_max, right_max = max(left_max, height[left]),\
                                  max(right_max, height[right])

            if left_max <= right_max:
                water += (left_max - height[left])
                left += 1
            else:
                water += (right_max - height[right])
                right -= 1

        return water

    # stack
    # n


if __name__ == '__main__':
    s = Solution()
    h = [4,2,0,3,2,5]
    print(s.trap(h))
