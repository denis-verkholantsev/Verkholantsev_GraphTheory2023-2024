from edmonds_karp import Graph
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

# Get the parent directory path
parent_dir = os.path.dirname(current_dir)

# Specify the relative path to the directory containing the files
files_dir = os.path.join(parent_dir, 'MaxFlow-tests')


file = "test_1.txt"
f = open(f'{files_dir}/{file}', mode = 'r')
N, M = map(int, f.readline().split())
graph = Graph(N)
# graph_nx = nx.DiGraph()
for _ in range(M):
    u, v, cap = map(int, f.readline().rstrip().split(' '))
    graph.add_edge(u-1, v-1, cap)
    # graph_nx.add_edge(u-1, v-1, capacity=cap)
f.close()

print(graph.max_flow_edmonds_karp(0, N-1))