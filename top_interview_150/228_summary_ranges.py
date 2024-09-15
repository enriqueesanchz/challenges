from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        n = len(nums)

        res = []
        curr = ""
        while i < n:
            if curr == "":
                curr += str(nums[i])
            else:
                if i == n-1 or nums[i+1] - nums[i] > 1:
                    if curr != str(nums[i]):
                        curr += "->" + str(nums[i])
                    
                    res.append(curr)
                    curr = ""
                
                i += 1

        return res
