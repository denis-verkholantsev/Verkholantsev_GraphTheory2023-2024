import DinicAlg as da
import networkx as nx
import pytest as pt
from timeit import default_timer as timer
from numpy import random
import sys

def func(n, m, u):
    G = nx.gnm_random_graph(n, m, directed=True)
    C = random.randint(1, u, size= m)
    g = da.Graph(n)
    i = 0
    for e in G.edges():
        g.addEdge(e[0], e[1], C[i])
        i += 1
    start = timer()
    max_flow = g.DinicMaxflow(0, n-1)
    end = timer()
    return [max_flow, end-start]

def test_1():
    n = 10
    m = 20
    u = 30
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("\n test_1: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_2():
    n = 10
    m = 40
    u = 30
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_2: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_3():
    n = 10
    m = 80
    u = 30
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_3: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_4():
    n = 50
    m = 100
    u = 50
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_4: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_5():
    n = 50
    m = 200
    u = 50
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_5: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_6():
    n = 50
    m = 400
    u = 50
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_6: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_7():
    n = 100
    m = 200
    u = 100
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_7: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_8():
    n = 100
    m = 400
    u = 100
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_8: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_9():
    n = 100
    m = 800
    u = 100
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_9: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_10():
    n = 10
    m = 90
    u = 30
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_10: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_11():
    n = 20
    m = 90
    u = 30
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_11: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_12():
    n = 40
    m = 90
    u = 30
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_12: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_13():
    n = 50
    m = 2450
    u = 100
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_13: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_14():
    n = 100
    m = 2450
    u = 100
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_14: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_15():
    n = 200
    m = 2450
    u = 100
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_15: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_16():
    n = 100
    m = 9900
    u = 100
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_16: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_17():
    n = 200
    m = 9900
    u = 100
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_17: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)

def test_18():
    n = 400
    m = 9900
    u = 100
    t = 0
    t_max = 0
    for i in range(50):
        res = func(n, m, u)
        t += res[1]
        if t_max < res[1]:
            t_max = res[1]
    print("test_18: average time =", t/50.0, " ,    max time =", t_max, ",    N =", n, ", M =", m, ", U =", u)



