from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        def backtrack(comb, k, nex):
            if k == 0:
                sol.append(comb.copy())
                return
            
            for i in range(nex, n+1):
                comb.append(i)
                backtrack(comb, k-1, i+1)
                comb.pop()

        backtrack([], k, 1)
        return sol
