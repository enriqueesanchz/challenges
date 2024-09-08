from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)-1

        while left != right+1:
            if nums[right] == val:
                right -= 1
            else:
                if nums[left] == val:
                    temp = nums[right]
                    nums[right] = nums[left]
                    nums[left] = temp
                
                left += 1

        return left

