from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degs = [0] * n
        for r1, r2 in roads:
            degs[r1] += 1
            degs[r2] += 1

        degs.sort(reverse=True)
        sum = 0
        for i in range(n):
            sum += (n - i) * degs[i]

        return sum
