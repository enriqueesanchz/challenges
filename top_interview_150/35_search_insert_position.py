from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        
        while l < r:
            m = l + (r - l) // 2
            
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m
            else:
                l = m+1

        return l
