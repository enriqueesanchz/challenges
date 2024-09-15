from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        sol = []
        curr = intervals[0]
        for i in range(n+1):
            if i == n:
                sol.append(curr)
                break

            mx = curr[1]
            mn = intervals[i+1][0]

            if mx >= mn:
                curr[1] = max(curr[1], intervals[i+1][1])
            else:
                sol.append(curr)
                curr = intervals[i+1]
        
        return sol
