import os

def load_adjacency_list(file_path):
    adjacency_list = {}
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                line = line.strip()
                if line:
                    nodes = line.split(':')
                    if len(nodes) == 2:
                        source = nodes[0].strip()
                        destinations = nodes[1].split(',')
                        destinations = [dest.strip() for dest in destinations]
                        adjacency_list[source] = destinations
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except UnicodeDecodeError:
        print(f"Error: Unable to decode file at {file_path}")
    return adjacency_list

def find_maximum_subgraph(adj_list1, adj_list2):
    # Find common nodes between the two graphs
    common_nodes = set(adj_list1.keys()).intersection(adj_list2.keys())

    # Identify common edges of the common nodes
    max_subgraph = {}
    for node in common_nodes:
        edges1 = adj_list1.get(node, [])
        edges2 = adj_list2.get(node, [])
        max_subgraph[node] = [edge for edge in edges1 if edge in common_nodes and edge in edges2]

    return max_subgraph

def find_all_mcs(folder_path, output_folder):
    files = os.listdir(folder_path)
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            file1_path = os.path.join(folder_path, files[i])
            file2_path = os.path.join(folder_path, files[j])
            adj_list1 = load_adjacency_list(file1_path)
            adj_list2 = load_adjacency_list(file2_path)
            mcs = find_maximum_subgraph(adj_list1, adj_list2)
            output_file = os.path.join(output_folder, f"{files[i]}_{files[j]}_mcs.txt")
            with open(output_file, 'w') as f:
                for node, edges in mcs.items():
                    f.write(f"{node}: {','.join(edges)}\n")

#folder_path = './directedGraph/HealthandFitness'
#output_folder = './mcs_results/HealthandFitness'

#folder_path = './directedGraph/ScienceandEducation'
#output_folder = './mcs_results/ScienceandEducation'

folder_path = './directedGraph/BusinessandFinance'
output_folder = './mcs_results/BusinessandFinance'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

find_all_mcs(folder_path, output_folder)
