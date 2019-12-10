from util.intcode import IntcodeMachine

init_mem = [int(instr) for instr in open('input.txt').read().strip().split(',')]

comp = IntcodeMachine(init_mem, 2)
comp.run()
print(comp.output)
