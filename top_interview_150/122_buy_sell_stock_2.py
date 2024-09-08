from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day = 0
        profit = 0

        while day < len(prices) - 1:
            if prices[day] < prices[day+1]:
                profit += prices[day+1] - prices[day]
            
            day += 1
        
        return profit

