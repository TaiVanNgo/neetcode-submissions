class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0 # L = buy, R = sell
        maxProfit = 0

        for R in range(1, len(prices)):
            if prices[L] < prices[R]:
                maxProfit = max(maxProfit, prices[R] - prices[L])
            else:
                L = R
        

        return maxProfit