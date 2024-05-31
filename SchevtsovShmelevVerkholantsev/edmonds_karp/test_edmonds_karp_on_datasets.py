from edmonds_karp import Graph
import pytest as pt
import numpy as np
import networkx as nx
from timeit import default_timer
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
files_dir = os.path.join(parent_dir, 'MaxFlow-tests')

files = sorted(os.listdir(files_dir))

def create_np(file):
    f = open(f'{files_dir}/{file}')
    N, M = map(int, f.readline().rstrip().split())
    graph: Graph = Graph(N)
    graph_nx = nx.DiGraph()
    for _ in range(M):
        u, v, cap = map(int, f.readline().rstrip().split())
        graph.add_edge(u-1, v-1, cap)
        graph_nx.add_edge(u-1, v-1, capacity=cap)

    return graph, graph_nx, N, M
      
@pt.mark.parametrize('path', files)
def test_graph(path):
    graph, graph_nx, N, M = create_np(path)
    start = default_timer()
    res = graph.max_flow_edmonds_karp(0, N - 1)
    stop = default_timer()
    res_nx = nx.maximum_flow_value(graph_nx, 0, N - 1, capacity="capacity")
    print(f'{path},  time: {stop - start}, N = {N}, M = {M}, maxflow = {res}, maxflow_nx = {res_nx}')
    assert res == res_nx

    

    


