from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        sm = 0
        for i in range(k):
            sm += nums[i]

        n = len(nums)
        mx = sm
        for i in range(k, n):
            sm = sm - nums[i-k] + nums[i]
            mx = max(mx, sm)

        return mx/k
