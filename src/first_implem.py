import networkx as nx

def toGraph(C):
    G = nx.Graph()
    T = []
    for champion in C:
        for trait in champion.traits:
            if not trait in T:
                T.append(trait)
    G.add_nodes_from(T)
    for champion in C:
        if G.get_edge_data(champion.traits[0], champion.traits[1]) is None:
            G.add_edge(champion.traits[0], champion.traits[1])
    return G

def compute(G):
    result = 0
    while G.edges():
        node = None
        for n in G.nodes():
            if node == None || len(G.neighbors(n)) < len(G.neighbors(node):
                node = n
        if len(G.neighbors(node)) != 0:
            other = None
            for n in G.neighbors(node):
                if other == None || len(G.neighbors(n)) < len(G.neighbors(other):
                    other = n
            result += 1
            G.remove_node(node)
            G.remove_node(other)
        else:
            G.remove_node(node)
    return result
