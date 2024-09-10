from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = 1
        y = 1
        pre = [1 for _ in range(len(nums))]
        suf = [1 for _ in range(len(nums))]

        for i in range(len(nums)-1):
            x = x * nums[i]
            pre[i+1] = x

            y = y * nums[-i-1]
            suf[1+i-len(nums)] = y

        sol = []
        for i in range(len(nums)):
            sol.append(pre[i] * suf[-i-1])

        return sol

