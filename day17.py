from util.intcode import IntcodeMachine

mem = [int(number) for number in open('input.txt').readline().split(',')]

comp = IntcodeMachine(mem)

# comp.run()

# adj = [1, -1, 1j, -1j]
# walls = set()
# pos = 0

# for instr in comp.output:
#     print(chr(instr), end='')

#     if instr == 35: walls.add(pos)

#     if instr == 10: pos = complex(0, pos.imag + 1)
#     else: pos += 1

# align = 0
# for wall in walls:
#     is_inter = True
#     for a in adj:
#         if wall + a not in walls: is_inter = False

#     if is_inter: align += wall.real * wall.imag

# print(int(align))

comp.memory[0] = 2
sol = [ord(c) for c in 'A,B,B,A,B,C,A,C,B,C\nL,4,L,6,L,8,L,12\nL,8,R,12,L,12\nR,12,L,6,L,6,L,8\nn\n']
comp.add_input(sol)
comp.run()
print(comp.output[-1])