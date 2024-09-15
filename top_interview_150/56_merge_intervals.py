from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)

        sol = []
        curr = intervals[0]
        while i < n:
            if i == n-1:
                sol.append(curr)
                break

            mx = curr[1]
            mn = intervals[i+1][0]

            if mx >= mn:
                curr[1] = max(curr[1], intervals[i+1][1])
            else:
                sol.append(curr)
                curr = intervals[i+1]
            i += 1

        return sol
