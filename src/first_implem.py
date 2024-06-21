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
            G.add_edge(champion.traits[0], champion.traits[1], champ=champion)
    return G

def compute(G):
    result = []
    while G.edges():
        node = None
        for n in G.nodes():
            if node == None or len([a for a in G.neighbors(n)]) < len([b for b in G.neighbors(node)]):
                node = n
        if len([e for e in G.neighbors(node)]) != 0:
            other = None
            for n in G.neighbors(node):
                if other == None or len([c for c in G.neighbors(n)]) < len([d for d in G.neighbors(other)]):
                    other = n
            result.append(G.get_edge_data(node, other)['champ'])
            G.remove_node(node)
            G.remove_node(other)
        else:
            G.remove_node(node)
    return result

def approx(all):
    return compute(toGraph(all))
