from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)

        def extra(n):
            return n+extraCandies >= mx

        return list(map(extra, candies))
