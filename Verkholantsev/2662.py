from typing import List
import heapq

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:

        def bfs():
            dist = 0
            queue = []
            heapq.heappush(queue, (dist, start[0], start[1]))
            visited = set()
            comp = abs(target[0] - start[0]) + abs(target[1] - start[1])
            while queue:
                dist, x1, y1= heapq.heappop(queue)
                if dist >= comp:
                    continue
                if (x1, y1) in visited:
                    continue
                visited.add((x1, y1))
                for x2, y2, x3, y3, w in specialRoads:
                    heapq.heappush(queue, (dist + abs(x1 - x2) + abs(y1 -y2) + w ,x3, y3))

                comp = min(comp, dist + abs(target[0] - x1) + abs(target[1] - y1))
            return comp

        return bfs()

            
            
