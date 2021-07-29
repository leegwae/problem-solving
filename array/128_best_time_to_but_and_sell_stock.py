import sys


class Solution:
    # n^2
    # def maxProfit(self, prices: list[int]) -> int:
    #     size = len(prices)
    #
    #     profit = 0
    #     for i, price in enumerate(prices[:-1]):
    #         right_max = max(prices[i:])
    #         profit = max(profit, right_max - price)
    #
    #     return profit

    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            print(profit)
            
        return profit


if __name__ == "__main__":
    s = Solution()
    prices = [5,7,1,2]
    print(s.maxProfit(prices))