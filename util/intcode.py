class IntcodeSim():
    def __init__(self, instruction_list, phase):
        self.memory = instruction_list
        self.ip = 0
        self.no_args = {1: 2, 2: 2, 3: 0, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 99: 0}
        self.no_locs = {1: 1, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: 1, 8: 1, 99: 0}

        self.input = [phase]
        self.output = []

        self.reach_exit = False
        self.err_no_input = False

    def process(self):
        instr = self.memory[self.ip]
        opcode = instr % 100

        mode = []
        mode.append(instr % 1000 // 100)
        mode.append(instr % 10000 // 1000)
        mode.append(instr % 100000 // 10000)

        self.ip += 1

        args = []

        for i in range(self.no_args[opcode]):
            args.append(self.memory[self.ip] if mode[i] == 1 else self.memory[self.memory[self.ip]])
            self.ip += 1

        if self.no_locs[opcode]:
            loc = self.memory[self.ip] if mode[-1] == 0 else None
            self.ip += 1

        if opcode == 1:
            self.memory[loc] = args[0] + args[1]
        
        elif opcode == 2:
            self.memory[loc] = args[0] * args[1]
        
        elif opcode == 3:
            if len(self.input):
                self.memory[loc] = self.input[0]
                self.input = self.input[1:]
            else:
                self.err_no_input = True
                self.ip -= 2
        
        elif opcode == 4:
            self.output.append(args[0])

        elif opcode == 5:
            if args[0] != 0:
                self.ip = args[1]

        elif opcode == 6:
            if args[0] == 0:
                self.ip = args[1]
        
        elif opcode == 7:
            self.memory[loc] = 1 if args[0] < args[1] else 0

        elif opcode == 8:
            self.memory[loc] = 1 if args[0] == args[1] else 0
        
        elif opcode == 99:
            self.reach_exit = True

    def run(self):
        while not self.err_no_input and not self.reach_exit:
            self.process()

    def clear_output(self):
        self.output = []

    def provide_input(self, new_input):
        if len(new_input):
            self.err_no_input = False

        self.input += new_input