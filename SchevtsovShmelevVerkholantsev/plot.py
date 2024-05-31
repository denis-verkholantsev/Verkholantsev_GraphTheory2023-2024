import matplotlib.pyplot as plt
from tests import test_fixed_edges, test_fixed_vertices, test_fixed_div

def plot_fixed_edges(m, path):
    x, y1, y2 = test_fixed_edges(m)

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(x, y1, label='Edmonds karp', color='blue', marker='o')

    ax.plot(x, y2, label='Dinic', color='green', marker='o')

    ax.set_title(f'При количестве ребер m = {m}')
    ax.set_xlabel('кол-во вершин')
    ax.set_ylabel('среднее время')

    # Легенда
    ax.legend()

    # Сетка
    ax.grid(True)

    plt.tight_layout()

    plt.savefig(path) 


def plot_fixed_vertices(n, path):
    x, y1, y2, _ = test_fixed_vertices(n)

    fig, ax = plt.subplots(figsize=(8, 6)) 

    ax.plot(x, y1, label='Edmonds karp', color='blue', marker='o')

    ax.plot(x, y2, label='Dinic', color='green', marker='o')

    ax.set_title(f'При количестве вершин N = {n}')
    ax.set_xlabel('вероятность ребра между вершинами')
    ax.set_ylabel('среднее время')

    ax.legend()
    ax.grid(True)

    plt.tight_layout()
    plt.savefig(path)  



def plot_fixed_div(div, path):
    x, y1, y2 = test_fixed_div(div)

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(x, y1, label='Edmonds karp', color='blue', marker='o')

    ax.plot(x, y2, label='Dinic', color='green', marker='o')

    ax.set_title(f'При количестве ребер n*(n-1)/{div}')
    ax.set_xlabel('количество вершин')
    ax.set_ylabel('среднее время')

    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.savefig(path)
