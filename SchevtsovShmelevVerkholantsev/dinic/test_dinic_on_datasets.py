import DinicAlg as da
import networkx as nx
import pytest as pt
from timeit import default_timer as timer
import sys
import os
sys.setrecursionlimit(1500)

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
files_dir = os.path.join(parent_dir, 'MaxFlow-tests')

files = sorted(os.listdir(files_dir))

@pt.mark.parametrize('path', files)
def test(path):
    f = open("{0}/{1}".format(files_dir, path))
    n, m = f.readline().split(" ")
    n = int(n)
    m = int(m)
    g = da.Graph(n)
    G = nx.DiGraph()
    for i in range(m):
        buf = list(map(int, f.readline().split(" ")))
        g.addEdge(buf[0]-1, buf[1]-1, buf[2])
        G.add_edge(buf[0]-1, buf[1]-1, weight=buf[2])
    start = timer() 
    max_flow_our = g.DinicMaxflow(0, n-1)
    end = timer()
    max_flow_nx = nx.maximum_flow_value(G, 0, n-1, capacity="weight")
    print(f'{path},  time: {end - start}, N = {n}, M = {n}, maxflow = {max_flow_our}, maxflow_nx = {max_flow_nx}')
    assert max_flow_our == max_flow_nx
