from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        curr = 0
        gas = nums[curr]

        while gas > 0:
            gas -= 1
            curr += 1
            
            if nums[curr] > gas:
                gas = nums[curr]

            if curr == len(nums) - 1:
                return True
        
        return False

