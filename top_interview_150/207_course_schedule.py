from typing import List

class Solution:
    def build_adj(self, n, edges):
        adj_list = [[] for _ in range(n)]

        for c1, c2 in edges:
            adj_list[c2].append(c1)
        return adj_list

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = self.build_adj(numCourses, prerequisites)

        state = [0] * numCourses

        def has_cycle(v):
            if state[v] == 1:
                return False

            if state[v] == -1:
                return True

            state[v] = -1

            for i in adj_list[v]:
                if has_cycle(i):
                    return True

            state[v] = 1
            return False

        for v in range(numCourses):
            if has_cycle(v):
                return False

        return True
