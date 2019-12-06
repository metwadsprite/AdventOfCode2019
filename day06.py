import networkx as nx

with open('input.txt') as input_file:
    lines = input_file.readlines()

graphP1 = nx.DiGraph()
graphP2 = nx.Graph()

for it, line in enumerate(lines):
    lines[it] = line.strip().split(')')

graphP1.add_edges_from(lines)

def get_pred_sum(node):
    predecs = list(graphP1.predecessors(node))
    pred_sum = len(predecs)
    return sum([pred_sum + get_pred_sum(pred) for pred in predecs])

orbit_sum = sum([get_pred_sum(node) for node in graphP1.nodes])

print(orbit_sum)

graphP2.add_edges_from(lines)

path = nx.shortest_path(graphP2, 'YOU', 'SAN')

print(len(path[2:-1]))