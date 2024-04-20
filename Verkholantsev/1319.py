from typing import List
from collections import defaultdict
'''
В дереве обхода n-1 ребро, найдем сколько ребер не в дереве - ответ
или (кол-во компонент связности - 1)
'''

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n - 1 > len(connections):
            return -1
        
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u):
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v)

        visited = set() 

        connected_components = 0
        for u in range(n):
            if u not in visited:
                dfs(u)
                connected_components += 1
        
        return connected_components - 1
        
