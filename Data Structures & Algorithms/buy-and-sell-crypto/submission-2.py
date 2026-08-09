class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        maxProfit = 0

        while L < R and R < len(prices) and L < len(prices): 
            if prices[R] < prices[L]:
                L = R
                R += 1
            else:
                maxProfit = max(maxProfit, prices[R] - prices[L])
                R += 1

        return maxProfit



