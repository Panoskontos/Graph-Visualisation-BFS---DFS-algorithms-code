# fastest way to implement graph

# for visualisation
import networkx as nx
import matplotlib.pyplot as plt
# for bfs algorithm
from queue import Queue


class Graph:

    def __init__(self, Nodes):
        self.nodes = Nodes
        self.adj_list = {}

        for node in self.nodes:
            self.adj_list[node] = []

    # undirected graph
    def add_relashionship(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_graph(self):
        for node in self.nodes:
            print(node, '->', self.adj_list[node])

# ------------ example with people ----------------


nodes = ['Nikos', 'Panos', 'Taf', 'Waitress', 'Tzanakakis', 'Elli', 'Mikros']
graph = Graph(nodes)

graph.add_relashionship('Nikos', 'Panos')
graph.add_relashionship('Tzanakakis', 'Panos')
graph.add_relashionship('Nikos', 'Tzanakakis')
graph.add_relashionship('Taf', 'Tzanakakis')
graph.add_relashionship('Taf', 'Nikos')
graph.add_relashionship('Mikros', 'Nikos')
graph.add_relashionship('Mikros', 'Panos')
graph.add_relashionship('Taf', 'Waitress')
graph.add_relashionship('Elli', 'Panos')
graph.print_graph()


# Visualising our graph -------------------------------------
G = nx.Graph()
G.add_node('Nikos')
G.add_node('Panos')
G.add_node('Taf')
G.add_node('Mikros')
G.add_node('Tzanakakis')
G.add_node('Elli')
G.add_node('Waitress')

G.add_edge('Nikos', 'Panos')
G.add_edge('Tzanakakis', 'Panos')
G.add_edge('Nikos', 'Tzanakakis')
G.add_edge('Taf', 'Tzanakakis')
G.add_edge('Taf', 'Nikos')
G.add_edge('Mikros', 'Nikos')
G.add_edge('Mikros', 'Panos')
G.add_edge('Taf', 'Waitress')
G.add_edge('Elli', 'Panos')

nx.draw(G, with_labels=1)
plt.show()
# BFS code-----------------------------------------------------

visited = {}
# level =  distance from src
level = {}
parent = {}
bfs_output = []
queue = Queue()

for node in graph.nodes:
    visited[node] = False
    parent[node] = None
    level[node] = -1

# start with source panos
s = 'Panos'
visited[s] = True
level[s] = 0
parent[s] = None
queue.put(s)

while not queue.empty():
    # remove and return item from queue
    u = queue.get()
    bfs_output.append(u)
    for v in graph.adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)

# print(bfs_output)

# shortest distance
# print(level)
v = 'Waitress'
shortest_path = []
while v is not None:
    shortest_path.append(v)
    v = parent[v]
shortest_path.reverse()
# print(shortest_path)


# DFS code------------------------------------------------------------------------------
# graph to test dfs
nodes2 = ['a', 'b', 'c', 'd', 'e', 'f']
graph2 = Graph(nodes2)
graph2.add_relashionship('a', 'b')
graph2.add_relashionship('b', 'd')
graph2.add_relashionship('b', 'e')
graph2.add_relashionship('c', 'f')


color = {}
# White, Grey, Black
parent = {}

# start, end
trav_time = {}
dfs_output = []

for node in graph2.nodes:
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1, -1]

time = 0


def dfs_utils(u):
    global time
    color[u] = 'G'
    trav_time[u][0] = time
    dfs_output.append(u)

    for v in graph2.adj_list[u]:
        if color[v] == 'W':
            parent[v] = u
            dfs_utils(v)
    color[u] = 'B'
    trav_time[u][1] = time
    time += 1


dfs_utils('a')
print(dfs_output)
