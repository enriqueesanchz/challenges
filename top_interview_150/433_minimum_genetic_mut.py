from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        def ndif(gen1, gen2):
            return sum([1 for i in range(len(gen1)) if gen1[i] != gen2[i]])

        def pmut(gen1, bank):
            p = []
            for gen2 in bank:
                if ndif(gen1, gen2) == 1:
                    p.append(gen2)
            return p

        q = deque([(startGene, 0)])
        visited = set()
        
        while q:
            curr, n = q.popleft()
            visited.add(curr)

            if curr == endGene:
                return n

            pmuts = pmut(curr, bank)
            if pmuts != None:
                for p in pmuts:
                    if p not in visited:
                        q.append((p, n+1))

        return -1
