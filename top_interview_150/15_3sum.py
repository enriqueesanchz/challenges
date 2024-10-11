from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        n = len(nums)

        for i in range(n):
            if i == 0 or nums[i] != nums[i-1]:
                target = -nums[i]
                for two in self.twoSum(nums[i+1:], target):
                    two.append(nums[i])
                    sol.append(two)
        return sol

    def twoSum(self, nums: List[int], target) -> List[List[int]]:
        sol = []
        indexes = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in indexes:
                if [complement, nums[i]] not in sol:
                    sol.append([complement, nums[i]])
            indexes[nums[i]] = i

        return sol
