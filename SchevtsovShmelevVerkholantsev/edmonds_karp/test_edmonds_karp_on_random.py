from edmonds_karp import Graph
import networkx as nx
import pytest as pt
from timeit import default_timer as timer
from numpy import random

dataset = [(10, 20, 30), (20, 40, 10), (50, 250, 55), (50, 450, 15), (60, 700, 17), (100, 5000, 10), (200, 2000, 20), (500, 5000, 21)]


@pt.mark.parametrize('n, m ,u', dataset)
def test_random(n, m, u):
    graph_nx = nx.gnm_random_graph(n, m, directed=True)
    cap = random.randint(1, u, size= m)
    graph = Graph(n)
    for i, e in enumerate(graph_nx.edges()):
        graph.add_edge(e[0], e[1], cap[i])
        
    max_time = 0
    sum_time = 0
    num_of_tests = 50
    for _ in range(num_of_tests):
        start = timer()
        graph.max_flow_edmonds_karp(0, n-1)
        stop = timer()
        sum_time += stop - start
        max_time = max(max_time, stop - start)

    print(f'\nN = {n}, M = {n}, U = {u}, avg_time = {sum_time/num_of_tests}, max_time = {max_time}')
