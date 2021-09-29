from collections import defaultdict

class Solution:
    # 루프 돌며 찾아내기: O(n)
    # def numJewelsInStones(self, jewels: str, stones: str) -> int:
    #     count = 0
    #
    #     for ch in stones:
    #         if ch in jewels:
    #             count += 1
    #
    #     return count

    # sum 함수 사용하기: O(n)
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)


if __name__ == '__main__':
    s = Solution()
    jewels = 'aA'
    stones = 'aAAbbbb'
    print(s.numJewelsInStones(jewels, stones))
