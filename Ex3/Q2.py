# BFS algorithm in Python


import collections
from typing import Callable
import doctest

"""This function is used to traverse a graph using certain algorithms such as DFS or BFS ,
would be nice to add dijkstra and **kawrgs for later use"""
def graph_traversal(algo: Callable, inpt, output: type(""), **kwargs):
    """
    >>> print(graph_traversal(bfs, {0: [1, 2], 1: [2], 2: [3], 3: [1, 2], 4: [5, 6]}, "length"))
    Not in graph:5
    Not in graph:6
    7
    >>> print(graph_traversal(bfs, {0: [1, 2], 1: [2], 2: [3], 3: [1, 2], 4: [5, 6]}, "trip"))
    Not in graph:5
    Not in graph:6
    [0, 1, 2, 3, 4, 5, 6]
    >>> print(graph_traversal(bfs, {0: [1, 2], 1: [2], 2: [3], 3: [1, 2], 4: []}, "trip"))
    [0, 1, 2, 3, 4]
    >>> print(graph_traversal(bfs, {0: [1, 2], 1: [2], 2: [3], 3: [1, 2], 4: [5,6],5:[6],6:[]}, "trip"))
    [0, 1, 2, 3, 4, 5, 6]
    >>> print(graph_traversal(DFS, {0: [1, 2], 1: [2], 2: [3], 3: [1, 2], 4: []}, "trip"))
    [0, 1, 2, 3, 4]
    >>> g = Graph()
    >>> g.addEdge(0, 1)
    >>> g.addEdge(0, 2)
    >>> g.addEdge(1, 2)
    >>> g.addEdge(2, 0)
    >>> g.addEdge(2, 3)
    >>> g.addEdge(3, 3)
    >>> print(graph_traversal(DFS,g,"trip"))
    [0, 1, 2, 3]
    >>> print(graph_traversal(bfs,g,"trip"))
    [0, 1, 2, 3]
    """
    graph = []
    if isinstance(inpt, Graph):
        graph = inpt.graph
    else:
        graph = inpt
    ans = algo(graph, **kwargs)
    if output == "trip":
        return list(ans)
    return len(ans)


'''
Generic Function for BFS traversal of a Graph
 (valid for directed as well as undirected graphs
 which can have multiple disconnected components)
for entire graph
'''


def bfs(graphs: dict):
    bfs_traversal = []
    visited = []  # [False] * V
    for node in graphs.keys():

        # To check if already visited
        if node not in visited:
            que = []
            visited.append(node)
            que.append(node)
            # BFS starting from ith node
            while len(que) > 0:
                g_node = que.pop(0)

                bfs_traversal.append(g_node)
                try:
                    for it in graphs[g_node]:
                        if it not in visited:
                            visited.append(it)
                            que.append(it)
                except Exception as e:
                    print("Not in graph:" + str(e))
    return bfs_traversal


def DFSUtil(graphs, v, visited):
    # Mark the current node as visited
    # and print it
    visited.add(v)
    # Recur for all the vertices
    # adjacent to this vertex
    try:
        for neighbour in graphs[v]:
            if neighbour not in visited:
                DFSUtil(graphs, neighbour, visited)
    except Exception as e:
        print("Not in graph:" + str(e))


def DFS(graphs: dict):
    # create a set to store all visited vertices
    visited = set()
    # call the recursive helper function to print DFS traversal starting from all
    # vertices one by one
    for vertex in graphs:
        if vertex not in visited:
            DFSUtil(graphs, vertex, visited)
    return visited


class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = collections.defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


if __name__ == '__main__':
    doctest.testmod()

