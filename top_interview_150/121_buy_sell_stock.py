from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int | float:
        
        bp = float('inf')
        profit = 0

        for p in prices:
            if p < bp:
                bp = p
            
            if profit < p - bp:
                profit = p - bp
        
        return profit

