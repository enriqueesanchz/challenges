from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int | None:
        count = 0
        candidate = None
        
        for i in nums:
            if count == 0:
                candidate = i
            
            if i == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

