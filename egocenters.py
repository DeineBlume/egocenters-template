import networkx as nx

def find_impostor(edgelist, pseudocenters):
    G = nx.Graph()
    G.add_edges_from(edgelist)
    central_dict = nx.degree_centrality(G)
    check = {a: central_dict[a] for a in pseudocenters}
    return sorted(check.items(), key=lambda x: x[1])[0][0]
