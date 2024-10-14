from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        indexes = {}
        for i in range(n):
            if nums[i] in indexes and i - indexes[nums[i]] <= k:
                return True
            
            indexes[nums[i]] = i

        return False
