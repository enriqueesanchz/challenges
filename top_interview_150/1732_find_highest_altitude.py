from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        mx = 0
        c = 0
        for m in gain:
            c += m
            mx = max(mx, c)

        return mx
