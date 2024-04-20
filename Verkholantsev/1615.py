from typing import List
from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        edges = defaultdict(set)
        for r1, r2 in roads:
            edges[r1].add(r2)
            edges[r2].add(r1)
        
        max_rank = 0
        for i in range(n):
            for j in range(i+1, n):
                max_rank = max(len(edges[i]) + len(edges[j]) - (i in edges[j]), max_rank)
            
        return max_rank
