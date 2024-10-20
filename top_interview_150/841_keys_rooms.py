from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()

        def visit(n):
            if n in visited:
                return

            visited.add(n)

            for k in rooms[n]:
                visit(k)

        visit(0)
        return list(visited) == [i for i in range(len(rooms))]
