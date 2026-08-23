class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0] #we will start with index zero
        max_profit = 0 # starting at zero since worst case scenario should be not making a transaction therefore profit = 0

        for price in prices:
            profit = price - buy_price
            max_profit = max(max_profit, profit)
            buy_price = min(buy_price, price) # buy price will become the lowest
        return max_profit

        # O(n) verus O(n^2)
        
            
        