class Edge:
    def __init__(self, v, flow, C, rev):
        self.v = v
        self.flow = flow
        self.C = C
        self.rev = rev

class Graph:
    def __init__(self, V):
        self.adj = {i: {} for i in range(V)}
        self.V = V
        self.level = [0 for i in range(V)]

    def addEdge(self, u, v, C):
        if v in self.adj[u]:
            self.adj[u][v].C += C
        else:
            a = Edge(v, 0, C, u)
            b = Edge(u, 0, 0, v)
            self.adj[u][v] = a
            self.adj[v][u] = b

    def BFS(self, s, t):
        for i in range(self.V):
            self.level[i] = -1

        self.level[s] = 0

        q = [s]
        while q:
            u = q.pop(0)
            for v in self.adj[u]:
                e = self.adj[u][v]
                if self.level[v] < 0 and e.flow < e.C:
                    self.level[v] = self.level[u] + 1
                    q.append(v)

        return self.level[t] >= 0

    def sendFlow(self, u, flow, t, start):
        if u == t:
            return flow

        for v in list(self.adj[u].keys())[start[u]:]:
            e = self.adj[u][v]
            if self.level[v] == self.level[u] + 1 and e.flow < e.C:
                curr_flow = min(flow, e.C - e.flow)
                temp_flow = self.sendFlow(v, curr_flow, t, start)

                if temp_flow > 0:
                    e.flow += temp_flow
                    self.adj[v][u].flow -= temp_flow
                    return temp_flow
            start[u] += 1

        return 0

    def DinicMaxflow(self, s, t):
        if s == t:
            return -1

        total = 0

        while self.BFS(s, t):
            start = {i: 0 for i in range(self.V)}
            while True:
                flow = self.sendFlow(s, float('inf'), t, start)
                if flow == 0:
                    break
                total += flow

        return total


