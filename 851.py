from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        edges = [[] for _ in range(len(quiet))]
        for a, b in richer:
            edges[b].append(a)
        
        visited = [False for _ in range(len(quiet))]
        res_mins = quiet.copy()
        res_idxs = [i for i in range(len(quiet))]
        def dfs(u):
            visited[u] = True
            for v in edges[u]:
                if not visited[v]:
                    dfs(v)
                if res_mins[v] < res_mins[u]:
                    res_mins[u] = res_mins[v]
                    res_idxs[u] = res_idxs[v]

        for i in range(len(visited)):
            if visited[i]:
                continue
            dfs(i)
        
        return res_idxs