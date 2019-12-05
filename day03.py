def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


wires = set()
# wires.add((0, 0, 0))
wires_lenghts = dict()
wires_lenghts[(0, 0)] = 0
min_dist = []
min_wire_dist = []
with open('input.txt') as input_file:
    line_id = 0
    for line in input_file:
        line_id += 1
        cur_point = [0, 0]
        line = line.split(',')
        wire_len = 0
        
        for instr in line:
            direction = instr[0]
            distance = int(instr[1:])
            
            for i in range(0, distance):
                if direction == 'U':
                    cur_point[1] += 1
                elif direction == 'D':
                    cur_point[1] -= 1
                elif direction == 'L':
                    cur_point[0] -= 1
                elif direction == 'R':
                    cur_point[0] += 1

                wire_len += 1

                if (cur_point[0], cur_point[1], 1) in wires and line_id >= 2:
                    min_dist.append(man_dist(cur_point, [0, 0]))
                    min_wire_dist.append(wire_len + wires_lenghts[(cur_point[0], cur_point[1])])
                else:
                    wires.add((cur_point[0], cur_point[1], line_id))
                    wires_lenghts[(cur_point[0], cur_point[1])] = wire_len

print(min(min_dist))
print(min(min_wire_dist))