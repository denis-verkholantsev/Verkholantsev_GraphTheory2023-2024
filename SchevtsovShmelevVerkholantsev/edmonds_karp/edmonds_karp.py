from collections import deque

class Graph: 
   
    def __init__(self, size):
        self.adj_dict = {}
        self.size = size

    def add_edge(self, u, v, cap):
        if u not in self.adj_dict:
            self.adj_dict[u] = {}
        
        if self.adj_dict.get(u).get(v):
            self.adj_dict[u][v] += cap
        else:    
            self.adj_dict[u][v] = cap
        
        if v not in self.adj_dict:
            self.adj_dict[v] = {}
        if u not in self.adj_dict[v]:
            self.adj_dict[v][u] = 0
        

    def max_flow_edmonds_karp(self, source, sink): 
        parent = [-1] * self.size
        max_flow = 0

        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.adj_dict[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.adj_dict[u][v] -= path_flow
                if v not in self.adj_dict:
                    self.adj_dict[v] = {}
                if u not in self.adj_dict[v]:
                    self.adj_dict[v][u] = 0
                self.adj_dict[v][u] += path_flow
                v = parent[v]

            
        return max_flow
    
    def BFS(self, source, target, parent): 
        visited = [False] * self.size
        
        queue = deque()
        
        queue.append(source) 
        visited[source] = True
        while queue: 

            u = queue.popleft() 
          
            if self.adj_dict.get(u):
                for v, cap in self.adj_dict[u].items():
                    if not visited[v] and cap > 0:
                        queue.append(v)
                        parent[v] = u
                        visited[v] =True

        return visited[target]

