from typing import List
from collections import deque


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque(initialBoxes)
        visited = set()
        total = 0
        while queue:
            box = queue.popleft()
            if not status[box] and box in visited:
                break

            visited.add(box)
            if not status[box]:
                queue.append(box)
                continue

            for k in keys[box]:
                status[k] = 1

            total += candies[box]
            queue.extend(containedBoxes[box])

        return total
    

        
