import networkx as nx

def find_impostor(edgelist, pseudocenters):
    G = nx.Graph()
    G.add_edges_from(edgelist)
    centralities = nx.betweenness_centrality(G)
    centralitiy_of_inputs = {a: centralities[a] for a in pseudocenters}
    return sorted(centralitiy_of_inputs.items(), key=lambda x: x[1])[0][0]

# in this execution i have chosen the best centrality
if __name__ == "__main__":

    centers = [0, 107, 1684, 1912, 3437, 348, 3980, 414, 686, 698]
    pseudocenters = [0, 107, 1684, 1912, 3437, 348, 612, 3980, 414, 686, 698]

    real_impostor = 612

    f = open('facebook_combined.txt')
    lines = f.readlines()

    def spl2(x):
        y = x.split()
        return (int(y[0]), int(y[1]))

    edges = list(map(spl2, lines))

    G = nx.Graph()
    G.add_edges_from(edges)

    # this row was variated via centrality method
    central_dict = nx.betweenness_centrality(G)
    check = {a: central_dict[a] for a in pseudocenters}
    print('ours', *sorted(sorted(check.items(), key=lambda x: x[1])[:10]), sep="\n")
    print('theirs', sorted(centers))
