from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (x, y), v in zip(equations, values):
            graph[x][y] = v
            graph[y][x] = 1.0 / v

        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1

            if y in graph[x]:
                return graph[x][y]

            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i, y, visited)
                    if temp != -1:
                        return graph[x][i] * temp

            return -1

        sol = []
        for q in queries:
            sol.append(dfs(q[0], q[1], set()))

        return sol
