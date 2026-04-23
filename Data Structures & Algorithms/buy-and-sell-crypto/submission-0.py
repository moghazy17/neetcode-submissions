class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]

        profit = 0

        for stock in prices:
            if stock < buy: 
                buy = stock
            profit = max(stock - buy, profit)
        
        return profit
