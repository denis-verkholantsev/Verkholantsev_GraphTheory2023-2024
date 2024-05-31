import networkx as nx
import pytest as pt
import random
import dinic.dinic_algo as da
import edmonds_karp.edmonds_karp as ed
from timeit import default_timer


def test_fixed_edges(m):
    dataset = [n for n in range(100, 401, 25)]
    result_time_edmonds, result_time_dinic = [], []
    for n in dataset:
        graph_nx = nx.dense_gnm_random_graph(n, m)
        num_of_tests = 50
        sum_time = 0
        res_ed = 0
        caps = [random.randint(0, n) for i in range(len(graph_nx.edges(data=True)))]
        for _ in range(num_of_tests):
            graph = ed.Graph(n)

            for i, edge in enumerate(list(graph_nx.edges(data=True))):
                graph.add_edge(edge[0], edge[1], caps[i])

            start = default_timer()
            res_ed = graph.max_flow_edmonds_karp(0, n-1)
            sum_time += default_timer() - start

        result_time_edmonds.append(sum_time/num_of_tests)

        
        sum_time = 0
        res_dinic = 0
        for _ in range(num_of_tests):
            graph = da.Graph(n)

            for i, edge in enumerate(list(graph_nx.edges(data=True))):
                graph.addEdge(edge[0], edge[1], caps[i])
                
            start = default_timer()
            res_dinic = graph.DinicMaxflow(0, n-1)
            sum_time += default_timer() - start

        result_time_dinic.append(sum_time/num_of_tests)

        print(f'N = {n}, M = {m}, time_ed = {result_time_edmonds[-1]}, time_dinic ={result_time_dinic[-1]}  res_ed = {res_ed}, res_d = {res_dinic}')

    return dataset, result_time_edmonds, result_time_dinic


def test_fixed_vertices(n):
    probability = [p / 100 for p in range(5, 101, 5)]
    result_time_edmonds, result_time_dinic = [], []
    nums_of_edges = []
    for p in probability:
        graph_nx = nx.erdos_renyi_graph(n, p)
        num_of_tests = 50
        sum_time = 0
        res_ed = 0
        caps = [random.randint(0, n) for i in range(len(graph_nx.edges(data=True)))]
        nums_of_edges.append(len(graph_nx.edges(data=True)))

        for _ in range(num_of_tests):
            graph = ed.Graph(n)

            for i, edge in enumerate(list(graph_nx.edges(data=True))):
                graph.add_edge(edge[0], edge[1], caps[i])
                
            start = default_timer()
            res_ed = graph.max_flow_edmonds_karp(0, n-1)
            sum_time += default_timer() - start

        result_time_edmonds.append(sum_time/num_of_tests)
        
        res_dinic = 0
        sum_time = 0
        for _ in range(num_of_tests):
            graph = da.Graph(n)

            for i, edge in enumerate(list(graph_nx.edges(data=True))):
                graph.addEdge(edge[0], edge[1], caps[i])

            start = default_timer()
            res_dinic = graph.DinicMaxflow(0, n-1)
            sum_time += default_timer() - start

        result_time_dinic.append(sum_time/num_of_tests)

        print(f'N = {n}, P = {p}, time_ed = {result_time_edmonds[-1]}, time_dinic ={result_time_dinic[-1]}  res_ed = {res_ed}, res_d = {res_dinic},')

    return probability, result_time_edmonds, result_time_dinic, nums_of_edges




def test_fixed_div(div):
    dataset = [n for n in range(25, 201, 25)]
    result_time_edmonds, result_time_dinic = [], []
    for n in dataset:
        graph_nx = nx.dense_gnm_random_graph(n, n*(n-1)//div)
        num_of_tests = 50
        sum_time = 0
        res_ed = 0
        caps = [random.randint(0, n) for i in range(len(graph_nx.edges(data=True)))]
        for _ in range(num_of_tests):
            graph = ed.Graph(n)

            for i, edge in enumerate(list(graph_nx.edges(data=True))):
                graph.add_edge(edge[0], edge[1], caps[i])

            start = default_timer()
            res_ed = graph.max_flow_edmonds_karp(0, n-1)
            sum_time += default_timer() - start

        result_time_edmonds.append(sum_time/num_of_tests)

        
        sum_time = 0
        res_dinic = 0
        for _ in range(num_of_tests):
            graph = da.Graph(n)

            for i, edge in enumerate(list(graph_nx.edges(data=True))):
                graph.addEdge(edge[0], edge[1], caps[i])
                
            start = default_timer()
            res_dinic = graph.DinicMaxflow(0, n-1)
            sum_time += default_timer() - start

        result_time_dinic.append(sum_time/num_of_tests)

        print(f'N = {n}, M = {n*(n-1)//div}, time_ed = {result_time_edmonds[-1]}, time_dinic ={result_time_dinic[-1]}  res_ed = {res_ed}, res_d = {res_dinic}')

    return dataset, result_time_edmonds, result_time_dinic
