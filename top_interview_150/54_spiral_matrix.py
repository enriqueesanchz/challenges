from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        res = []

        d = 'r'
        r, c = 0, 0
        for _ in range(m * n):
            res.append(matrix[r][c])
            matrix[r][c] = '.'

            if d == 'r' and (c == n-1 or matrix[r][c+1] == '.'):
                d = 'd'
            elif d == 'd' and (r == m-1 or matrix[r+1][c] == '.'):
                d = 'l'
            elif d == 'l' and (c == 0 or matrix[r][c-1] == '.'):
                d = 'u'
            elif d == 'u' and matrix[r-1][c] == '.':
                d = 'r'

            if d == 'r':
                c += 1
            elif d == 'd':
                r += 1
            elif d == 'l':
                c -= 1
            elif d == 'u':
                r -= 1
                
        return res
