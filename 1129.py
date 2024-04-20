from collections import deque, defaultdict
from typing import List
import sys

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(set)
        blue = defaultdict(set)

        for a, b in redEdges:
            red[a].add(b)

        for a, b in blueEdges:
            blue[a].add(b)

        def bfs():
            queue = deque([(0, 'r', 0), (0, 'b', 0)])
            visited = defaultdict(int)
            visited[0] = 0
            used = set()
            while queue:
                cur, color, dist = queue.popleft()
                visited[cur] = dist if dist < visited.get(cur, dist) else visited.get(cur, dist)
                next_color = 'b' if color == 'r' else 'r'
                next_vertices = red[cur] if color == 'b' else blue[cur]
                for next in next_vertices:
                    if ((cur, next, next_color)) not in used:
                        queue.append((next, next_color, dist + 1))
                        used.add((cur, next, next_color))
            return visited
        
        visited = bfs()

        return [visited[i] if i in visited else -1 for i in range(n)]
