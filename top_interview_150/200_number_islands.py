from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(grid, r, c):
            q = deque()
            q.append((r, c))
            directions = [[0,1], [1,0], [0,-1], [-1,0]]

            while q:
                row, col = q.popleft()
                for mr, mc in directions:
                    dr = row + mr
                    dc = col + mc
                    if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == '1':
                        grid[dr][dc] = '0'
                        q.append((dr, dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    grid[r][c] = '0'
                    bfs(grid, r, c)
        
        return islands
