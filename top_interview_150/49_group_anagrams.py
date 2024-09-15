from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)

        for s in strs:
            k = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                k[idx] += 1
            
            sol[tuple(k)].append(s)

        return sol.values()
