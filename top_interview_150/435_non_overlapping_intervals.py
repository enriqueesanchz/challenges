from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end = -1e5
        intervals.sort(key=lambda x: x[1])
        print(intervals)

        count = 0
        for i in range(len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                count +=1

        return count
