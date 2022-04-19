from typing import List
from collections import Counter

class Solution:
    # using counter
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     counter = [(num, count) for num, count in Counter(nums).items()]
    #     counter.sort(key=lambda x: x[1], reverse=True)
    #     return list(map(lambda x: x[0], counter))[:k]

    # using counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*Counter(nums).most_common(k)))[0]

if __name__ == '__main__':
    s = Solution()
    nums = [1]
    k = 1
    print(s.topKFrequent(nums, k))
