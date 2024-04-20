from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in range(len(rooms))]
        def dfs(u):
            visited[u] = True
            for v in rooms[u]:
                if not visited[v]:
                    dfs(v)
        dfs(0)
        return visited.count(True) == len(rooms)
