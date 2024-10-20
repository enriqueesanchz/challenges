from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sm1 = 0
        sm2 = sum(nums[1:])

        if sm1 == sm2:
            return 0

        for i in range(1, len(nums)):
            sm1 += nums[i-1]
            sm2 -= nums[i]

            if sm1 == sm2:
                return i

        return -1
