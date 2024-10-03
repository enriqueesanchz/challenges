from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for i in range(1, n):
            row = triangle[i-1]
            next_row = triangle[i]

            for j in range(len(next_row)):
                if j == 0:
                    next_row[j] += row[j]
                elif j == len(row):
                    next_row[j] += row[j-1]
                else:
                    next_row[j] += min(row[j-1], row[j])

        return min(triangle[-1])
