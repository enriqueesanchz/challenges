from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 1
        n = len(nums)

        sol = 1e10
        total = nums[0]
        while l <= r and r <= n:
            if total < target:
                r += 1
                if r == n+1:
                    break
                total += nums[r-1]
            else:
                sol = min(sol, r - l)
                total -= nums[l]
                l += 1
        
        if sol == 1e10:
            return 0
            
        return sol
