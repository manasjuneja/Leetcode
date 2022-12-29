class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = 9999999999
        profit = 0
        for i in prices:
            minp = min(minp, i)
            profit = max(profit, i - minp)

        return profit
