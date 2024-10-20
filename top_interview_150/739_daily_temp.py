from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            temp = temperatures[i]

            while stack and stack[-1][0] < temp:
                idx = stack.pop()[1]
                ans[idx] = i - idx

            stack.append((temp, i))

        return ans
