"""
Step-1: Load in dictionary with keys as nodes and values as list
Step-2: Identify Common Nodes between the graphs
Step-3: Identify Common edges of the common nodes of the two graphs
Step-4: Store the Maximal Subgraph
"""
def load_adjacency_list(file_path):
    adjacency_list = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                nodes = line.split(':')
                if len(nodes) == 2:
                    source = nodes[0].strip()
                    destinations = nodes[1].split(',')
                    destinations = [dest.strip() for dest in destinations]
                    adjacency_list[source] = destinations
    return adjacency_list


def find_maximum_subgraph(adj_list1, adj_list2):
    #it will return the common nodes in the two graphs using intersection
    common_nodes = set(adj_list1.keys()).intersection(adj_list2.keys())

    max_subgraph = {}
    for node in common_nodes:
        edges1 = adj_list1.get(node, [])
        edges2 = adj_list2.get(node, [])
        max_subgraph[node] = [edge for edge in edges1 if edge in common_nodes and edge in edges2]

    return max_subgraph



breakingmuscle_adj_list = load_adjacency_list('./directedGraph/breakingmuscle.txt')
nerdfitness_adj_list = load_adjacency_list('./directedGraph/nerdfitness.txt')

maximum_subgraph = find_maximum_subgraph(breakingmuscle_adj_list, nerdfitness_adj_list)
print(maximum_subgraph)



