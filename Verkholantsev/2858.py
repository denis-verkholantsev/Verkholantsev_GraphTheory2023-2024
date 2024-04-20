from typing import List

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        
        edges = set(tuple(e) for e in edges)
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        answer = [0] * n
        func1 = lambda u, v: 1 if (v, u) in edges else 0
        func2 = lambda u, v: 1 if (u, v) in edges else -1
        def dfs(u, prev):
            for v in tree[u]:
                if v != prev:
                    answer[0] += func1(u, v)
                    dfs(v, u)

        def dfs2(u, prev):
            for v in tree[u]:
                if v != prev:
                    answer[v] = answer[u] + func2(u, v)
                    dfs2(v, u)

        dfs(0, -1)
        dfs2(0, -1)

        return answer
    
