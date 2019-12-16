from util.intcode import IntcodeMachine
import os
import networkx

def visualize():
    os.system('cls')
    for i in range(-21, 20):
        for j in range(-21, 20):
            if complex(j, i) in walls: print('██', end='')
            elif complex(j, i) == end: print('XX', end='')
            elif complex(j, i) == pos: print('##', end='')
            elif complex(j, i) in visited: print('..', end='')
            else: print('  ', end='')
        print()

mem = [int(number) for number in open('input.txt').readline().split(',')]

droid  = IntcodeMachine(mem)
pos = 0
walls = set()
visited = set()

change_head = {1: 4, 4: 2, 2: 3, 3: 1}
inv_change_head = {1: 3, 3: 2, 2: 4, 4: 1}

change_pos = {1: -1j, 2: 1j, 3: -1, 4: 1}

head = 1

maze = networkx.Graph()
maze.add_node(pos)

while True:
    droid.clear_output()
    visited.add(pos)
    droid.add_input([head])

    droid.run()
    output = droid.output

    if output[0] == 0:
        walls.add(pos + change_pos[head])
        head = inv_change_head[head]
    else:
        maze.add_edge(pos, pos + change_pos[head])
        pos += change_pos[head]
        head = change_head[head]

        if output[0] == 2: end = pos
        if pos == 0: break

visualize()

max_dist = 0
for tar in maze:
    max_dist = max(max_dist, len(networkx.shortest_path(maze, end, tar)) - 1)

print(len(networkx.shortest_path(maze, 0, end)) - 1)
print(max_dist)