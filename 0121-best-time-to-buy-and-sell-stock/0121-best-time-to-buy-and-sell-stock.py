class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        stock = 0
        for idx in range(1,len(prices)):
            if prices[idx]<mini:
                mini=prices[idx]
            else:
                stock = max(stock,prices[idx]-mini)

        return stock