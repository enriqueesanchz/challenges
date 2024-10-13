from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        neig = [[0] * m for _ in range(n)] 
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    if i+1 < n:
                        neig[i+1][j] += 1
                    if j+1 < m:
                        neig[i][j+1] += 1
                    if i+1 < n and j+1 < m:
                        neig[i+1][j+1] += 1
                    if i-1 >= 0:
                        neig[i-1][j] += 1
                    if j-1 >= 0:
                        neig[i][j-1] += 1
                    if i-1 >= 0 and j-1 >= 0:
                        neig[i-1][j-1] += 1
                    if i+1 < n and j-1 >= 0:
                        neig[i+1][j-1] += 1
                    if i-1 >= 0 and j+1 < m:
                        neig[i-1][j+1] += 1

        for i in range(n):
            for j in range(m):
                if neig[i][j] < 2:
                    board[i][j] = 0
                elif neig[i][j] == 3:
                    board[i][j] = 1
                elif neig[i][j] > 3:
                    board[i][j] = 0
                elif board[i][j] == 1 and neig[i][j] == 2:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
