from collections import defaultdict
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ocurr = defaultdict(int)

        for num in arr:
            ocurr[num] += 1

        times = set()
        for _, v in ocurr.items():
            if v in times:
                return False
            times.add(v)

        return True
