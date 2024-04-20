from typing import List
from collections import defaultdict

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def union(u: int, v: int, size: List[int], p: List[int]):
            u = find(u, p)
            v = find(v, p)
            if u == v:
                return False
            
            if size[u] > size[v]:
                size[u] += size[v]
                p[v] = u
            else:
                size[v] += size[u]
                p[u] = v

            return True
            
        def find(u: int, p: List[int]):
            if u != p[u]:
                p[u] = find(p[u], p)
            return p[u]

        p_a, p_b = [i for i in range(n)], [i for i in range(n)]
        size_a, size_b = [1] * n, [1] * n
        unused = 0
        for t, u, v in edges:
            if t == 3:
                if union(u-1, v-1, size_a, p_a):
                    union(u-1, v-1, size_b, p_b)
                else:
                    unused += 1
        
        for t, u, v in edges:
            if t == 1 and not union(u-1, v-1, size_a, p_a) or t == 2 and not union(u-1, v-1, size_b, p_b):
                unused += 1
        
        return unused if max(size_a) == n and max(size_b) == n else -1
        


        
