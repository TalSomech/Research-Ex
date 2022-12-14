import matplotlib.pyplot as plt
import networkx as nx


# Recursive Function to find the
# Maximal Independent Vertex Set
def graphSets(graph: nx.Graph):
    # Base Case - Given Graph
    # has no nodes
    if graph.size() == 0:
        return []

    # Base Case - Given Graph
    # has 1 node
    if graph.size() == 1:
        return list(graph.nodes)

    # Select a vertex from the graph
    vCurrent = list(graph.nodes)[0]

    # Case 1 - Proceed removing
    # the selected vertex
    # from the Maximal Set
    graph2 = graph.copy()
    graph2.remove_node(vCurrent)
    # Delete current vertex
    # from the Graph
    # del graph2[vCurrent]

    # Recursive call - Gets
    # Maximal Set,
    # assuming current Vertex
    # not selected
    res1 = graphSets(graph2)

    # Case 2 - Proceed considering
    # the selected vertex as part
    # of the Maximal Set

    # Loop through its neighbours
    for v in graph.edges(vCurrent):
        # Delete neighbor from
        # the current subgraph
        if v in graph2:
            graph2.remove_node(v)

    # This result set contains VFirst,
    # and the result of recursive
    # call assuming neighbors of vFirst
    # are not selected
    res2 = [vCurrent] + graphSets(graph2)

    # Our final result is the one
    # which is bigger, return it
    if len(res1) > len(res2):
        return res1
    return res2


def graph_create():
    ns = [5, 10, 15, 20]
    ps = [0.25, 0.35, 0.50, 0.75, 1]
    fig, axes = plt.subplots(2, 2)
    i = 0
    j = 0

    for n in ns:

        tols = []
        for p in ps:
            graph = nx.gnp_random_graph(n, p)
            EXres = graphSets(graph)
            APXres = list(nx.approximation.maximum_independent_set(graph))
            if len(EXres) > 0:
                tol = len(APXres) / len(EXres)
            else:
                tol = 1
            tols.append(tol)
        axes[i, j].scatter(ps, tols)
        axes[i,j].title.set_text(n)
        if i == 0 and j == 0:
            j = j + 1
        elif i == 0 and j == 1:
            i = 1
        elif i == 1 and j == 1:
            j = 0
    plt.show()

if __name__ == '__main__':
    graph_create()
