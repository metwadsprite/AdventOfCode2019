class IntcodeMachine():
    class EmptyInput(Exception):
        def __init__(self):
                super().__init__("Machine input is empty. Can't continue.")

    def __init__(self, init_mem, init_input=None):
        self.memory = init_mem
        self.ip = 0
        self.no_args = {
            1: 2,
            2: 2,
            3: 0,
            4: 1,
            5: 2,
            6: 2,
            7: 2,
            8: 2,
            9: 1,
            99: 0
        }
        self.writes = {
            1: True,
            2: True,
            3: True,
            4: False,
            5: False,
            6: False,
            7: True,
            8: True,
            9: False,
            99: False
        }

        self.input = [init_input]
        self.output = []

        self.input_history = []
        self.output_history = []

        self.reached_exit = False

        self.relative_base = 0

        self.memory = {i: self.memory[i] for i in range(len(self.memory))}

    def step(self):
        instr = self.memory[self.ip]
        opcode = instr % 100

        mode = []
        mode.append(instr % 1000 // 100)
        mode.append(instr % 10000 // 1000)
        mode.append(instr % 100000 // 10000)

        self.ip += 1

        args = []
        mode_it = 0

        for i in range(self.no_args[opcode]):
            if self.ip not in self.memory:
                self.memory[self.ip] = 0
            if self.memory[self.ip] not in self.memory:
                self.memory[self.memory[self.ip]] = 0
            if self.relative_base + self.memory[self.ip] not in self.memory:
                self.memory[self.relative_base + self.memory[self.ip]] = 0

            if mode[mode_it] == 0:
                args.append(self.memory[self.memory[self.ip]])
            elif mode[mode_it] == 1:
                args.append(self.memory[self.ip])
            elif mode[mode_it] == 2:
                args.append(self.memory[self.relative_base + self.memory[self.ip]])
            
            self.ip += 1
            mode_it += 1

        if self.writes[opcode]:
            if mode[mode_it] == 0:
                loc = self.memory[self.ip]
            elif mode[mode_it] == 2:
                loc = self.relative_base + self.memory[self.ip]

            self.ip += 1

        if opcode == 1:
            self.memory[loc] = args[0] + args[1]
        
        elif opcode == 2:
            self.memory[loc] = args[0] * args[1]
        
        elif opcode == 3:
            if len(self.input):
                self.memory[loc] = self.input[0]
                del self.input[0]
            else:
                self.ip -= 2
                raise self.EmptyInput
        
        elif opcode == 4:
            self.output.append(args[0])
            self.output_history.append(args[0])

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

        elif opcode == 9:
            self.relative_base += args[0]
        
        elif opcode == 99:
            self.reached_exit = True

    def run(self):
        while not self.reached_exit:
            try:
                self.step()
            except self.EmptyInput:
                return

    def clear_output(self):
        self.output = []

    def add_input(self, new_input):
        self.input += new_input
        self.input_history += new_input