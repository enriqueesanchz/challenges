from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = [0 for _ in range(len(citations)+1)]

        for c in citations:
            c = min(c, len(h)-1)
            h[c] += 1
        
        total = 0
        for i in range(len(h) - 1, 0, -1):
            total += h[i]
            if total >= i:
                return i
        
        return 0

