with open('input.txt') as input_file:
    line = input_file.readline()

line = line.split(',')
line = [int(num) for num in line]

prog_input = 5
prog_output = [0]

reach_exit = 0

no_args = {1: 2, 2: 2, 3: 0, 4: 1, 99: 0, 5: 2, 6: 2, 7: 2, 8: 2}
no_locs = {1: 1, 2: 1, 3: 1, 4: 0, 99: 0, 5: 0, 6: 0, 7: 1, 8: 1}

def proc_instr(ip):
    instr = line[ip]
    opcode = instr % 100

    mode = []
    mode.append(instr % 1000 // 100)
    mode.append(instr % 10000 // 1000)
    mode.append(instr % 100000 // 10000)

    ip += 1

    args = []

    for i in range(no_args[opcode]):
        args.append(line[ip] if mode[i] == 1 else line[line[ip]])
        ip += 1

    if no_locs[opcode]:
        loc = line[ip] if mode[-1] == 0 else None
        ip += 1

    if opcode == 1:
        line[loc] = args[0] + args[1]
    
    elif opcode == 2:
        line[loc] = args[0] * args[1]
    
    elif opcode == 3:
        line[loc] = prog_input
    
    elif opcode == 4:
        prog_output.append(args[0])

    elif opcode == 5:
        if args[0] != 0:
            ip = args[1]

    elif opcode == 6:
        if args[0] == 0:
            ip = args[1]
    
    elif opcode == 7:
        line[loc] = 1 if args[0] < args[1] else 0

    elif opcode == 8:
        line[loc] = 1 if args[0] == args[1] else 0
    
    elif opcode == 99:
        reach_exit = 1

    return ip


ip = 0
while prog_output[-1] == 0 or reach_exit == 1:
    ip = proc_instr(ip)

print(prog_output)