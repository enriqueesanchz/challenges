from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        m = len(matrix[0])

        l = 0
        r = n * m
        
        while l < r:
            mid = l + (r-l)//2
            x = mid // m
            y = mid % m

            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                r = mid
            else:
                l = mid + 1

        return False
